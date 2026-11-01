import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const skillsDirectory = fileURLToPath(new URL("./skills/", import.meta.url));
const skillIds = ["managing-superpowers-backlog", "managing-superpowers-handoffs"];

function scalar(frontmatter, field) {
  const matches = [...frontmatter.matchAll(new RegExp(`^${field}:[ \\t]*([^\\r\\n]*)\\r?$`, "gm"))];
  if (matches.length !== 1) throw new Error(`expected one ${field}`);
  const value = matches[0][1].trim();
  if (!value || /^[>|[\]{}]/.test(value)) throw new Error(`expected scalar ${field}`);
  if (value.startsWith('"')) return JSON.parse(value);
  if (value.startsWith("'")) {
    if (!value.endsWith("'")) throw new Error(`unterminated ${field}`);
    return value.slice(1, -1).replaceAll("''", "'");
  }
  return value;
}

async function readSkills() {
  return Promise.all(skillIds.map(async (id) => {
    const source = path.join(skillsDirectory, id, "SKILL.md");
    let text;
    try {
      text = await fs.readFile(source, "utf8");
    } catch (cause) {
      throw new Error(`Cannot read canonical skill ${source}`, { cause });
    }
    try {
      const frontmatter = text.match(/^---\r?\n([\s\S]*?)\r?\n---\r?\n([\s\S]*)$/);
      if (!frontmatter) throw new Error("missing frontmatter");
      const name = scalar(frontmatter[1], "name");
      const description = scalar(frontmatter[1], "description");
      if (name !== id || typeof description !== "string" || !description.trim()) {
        throw new Error("invalid name or description");
      }
      return { id, name, description, path: source, content: frontmatter[2] };
    } catch (cause) {
      throw new Error(`Invalid canonical skill ${source}`, { cause });
    }
  }));
}

export const BackplanePlugin = async () => {
  await readSkills();
  return {
  config: async (config) => {
    config.skills ??= {};
    config.skills.paths ??= [];
    const directory = path.resolve(skillsDirectory);
    if (!config.skills.paths.includes(directory)) config.skills.paths.push(directory);
  },
  };
};

export default {
  id: "superpowers-backplane",
  server: BackplanePlugin,
  async setup(ctx) {
    if (typeof ctx?.skill?.transform !== "function") return;
    const skills = await readSkills();
    await ctx.skill.transform((editor) => {
      for (const skill of skills) editor.add(skill);
    });
  },
};
