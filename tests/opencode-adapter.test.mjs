import assert from "node:assert/strict";
import { test } from "node:test";
import fs from "node:fs/promises";
import path from "node:path";
import { pathToFileURL } from "node:url";

const root = path.resolve(import.meta.dirname, "..");
const names = ["managing-superpowers-backlog", "managing-superpowers-handoffs"];
const area = process.env.SP_BP_TEST_AREA;
assert.ok(area, "SP_BP_TEST_AREA must name the verified ignored fixture directory");

async function fixture() {
  const directory = await fs.mkdtemp(path.join(area, "adapter space "));
  for (const name of names) {
    await fs.mkdir(path.join(directory, "skills", name), { recursive: true });
    await fs.writeFile(path.join(directory, "skills", name, "SKILL.md"),
      `---\r\nname: ${name}\r\ndescription: Use when testing canonical ${name}.\r\n---\r\n\r\n# Body ${name}\r\n\r\nRead [reference](references/contract.md).\r\n`, "utf8");
  }
  await fs.writeFile(path.join(directory, "package.json"), '{"type":"module"}', "utf8");
  let module;
  await assert.doesNotReject(async () => {
    await fs.copyFile(path.join(root, "index.js"), path.join(directory, "index.js"));
    module = await import(pathToFileURL(path.join(directory, "index.js")).href);
  }, "the package entry point must load");
  return { directory, module };
}

test("v1_preserves_paths_and_registers_once", async () => {
  const { directory, module } = await fixture();
  const hooks = await module.BackplanePlugin({});
  const config = { skills: { paths: ["/unrelated/skills"], urls: ["https://example.invalid/skill"] }, plugin: ["unrelated"] };
  await hooks.config(config);
  await hooks.config(config);
  assert.deepEqual(config, { skills: { paths: ["/unrelated/skills", path.join(directory, "skills")], urls: ["https://example.invalid/skill"] }, plugin: ["unrelated"] });
  const empty = {};
  await hooks.config(empty);
  assert.deepEqual(empty, { skills: { paths: [path.join(directory, "skills")] } });
  assert.equal(module.default.server, module.BackplanePlugin);
});

test("v1_context_does_not_activate_v2", async () => {
  const { module } = await fixture();
  await assert.doesNotReject(() => module.default.setup({ client: {}, directory: "/fixture" }));
  await assert.doesNotReject(() => module.default.setup(undefined));
});

test("v2_registers_exact_canonical_payloads", async () => {
  const { directory, module } = await fixture();
  const actual = [];
  await module.default.setup({ skill: { transform: async (callback) => {
    const result = callback({ add: (entry) => actual.push(entry) });
    assert.equal(result, undefined, "transform callback must be synchronous");
  } } });
  assert.equal(module.default.id, "superpowers-backplane");
  assert.deepEqual(actual, names.map((name) => ({
    id: name, name, description: `Use when testing canonical ${name}.`,
    path: path.join(directory, "skills", name, "SKILL.md"),
    content: `\r\n# Body ${name}\r\n\r\nRead [reference](references/contract.md).\r\n`,
  })));
});

test("v2_replay_preserves_unrelated_skills", async () => {
  const { module } = await fixture();
  const sentinel = { id: "unrelated", name: "sentinel", content: "keep" };
  let transform;
  await module.default.setup({ skill: { transform: async (callback) => { transform = callback; } } });
  for (let replay = 0; replay < 2; replay++) {
    const entries = new Map([["unrelated", sentinel]]);
    transform({ add: (entry) => entries.set(entry.id, entry) });
    assert.equal(entries.get("unrelated"), sentinel);
    assert.deepEqual([...entries.keys()], ["unrelated", ...names]);
  }
});

test("paths_resolve_from_package_with_spaces_and_different_cwd", async () => {
  const script = await fs.readFile(path.join(root, "index.js"), "utf8").catch(() => null);
  assert.ok(script, "adapter source must exist");
  const { directory, module } = await fixture();
  const entries = [];
  await module.default.setup({ skill: { transform: async (callback) => callback({ add: (entry) => entries.push(entry) }) } });
  assert.ok(directory.includes("adapter space "));
  assert.notEqual(process.cwd(), directory);
  for (const entry of entries) {
    assert.equal(await fs.realpath(entry.path), await fs.realpath(path.join(directory, "skills", entry.id, "SKILL.md")));
    assert.equal(path.isAbsolute(entry.path), true);
    if (process.platform === "win32") assert.match(entry.path, /^[A-Za-z]:\\/);
  }
});


test("malformed_skill_rejects_before_any_registration", async () => {
  for (const source of ["no frontmatter", "---\nname: wrong-name\ndescription: Use when testing.\n---\nbody\n", "---\nname: managing-superpowers-handoffs\ndescription:\n---\nbody\n"]) {
    const { directory, module } = await fixture();
    await fs.writeFile(path.join(directory, "skills", names[1], "SKILL.md"), source);
    const entries = [];
    await assert.rejects(() => module.default.setup({ skill: { transform: async (callback) => callback({ add: (entry) => entries.push(entry) }) } }), /Invalid canonical skill/);
    assert.deepEqual(entries, []);
  }
});

test("missing_skill_rejects_before_any_registration", async () => {
  const { directory, module } = await fixture();
  await fs.unlink(path.join(directory, "skills", names[1], "SKILL.md"));
  const entries = [];
  await assert.rejects(() => module.default.setup({ skill: { transform: async (callback) => callback({ add: (entry) => entries.push(entry) }) } }), /Cannot read canonical skill/);
  assert.deepEqual(entries, []);
});

test("quoted_metadata_is_decoded_without_changing_body", async () => {
  const { directory, module } = await fixture();
  await fs.writeFile(path.join(directory, "skills", names[0], "SKILL.md"), `---\nname: "${names[0]}"\ndescription: 'Use when it''s canonical.'\n---\nBody preserved.\n`);
  const entries = [];
  await module.default.setup({ skill: { transform: async (callback) => callback({ add: (entry) => entries.push(entry) }) } });
  assert.equal(entries[0].name, "managing-superpowers-backlog");
  assert.equal(entries[0].description, "Use when it's canonical.");
  assert.equal(entries[0].content, "Body preserved.\n");
});


test("v1_rejects_broken_canonical_tree_before_config_mutation", async () => {
  const { directory, module } = await fixture();
  await fs.writeFile(path.join(directory, "skills", names[0], "SKILL.md"), "broken canonical skill");
  const config = { skills: { paths: ["/sentinel"] } };
  await assert.rejects(async () => {
    const hooks = await module.BackplanePlugin({});
    await hooks.config(config);
  }, /Invalid canonical skill/);
  assert.deepEqual(config, { skills: { paths: ["/sentinel"] } });
});
