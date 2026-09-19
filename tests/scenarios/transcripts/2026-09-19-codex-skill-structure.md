# Codex Skill Structure Conformance — Issue #3

- Date: 2026-09-19.
- Candidate Backplane branch: `feat/codex-installation-surface`; root manifest and main SKILL.md files began at package commit `8bfba888599568cc8f729ba6f0c030ace8e6377f`. The installation reference includes the Task 4 correction measured below.
- Host: Windows PowerShell 7.6.6, `codex-cli 0.155.1`.
- Upstream native package: `superpowers@superpowers-dev` 6.4.1 from `https://github.com/obra/superpowers.git`, tag `v6.4.1`; independent checkout revision `5bf4e78011075bcfc0dc295f0724994cd123ee71`.

## Exact checks

PowerShell read both canonical root `skills/*/SKILL.md` files. Each began and ended YAML frontmatter with `---`, had the exact folder-matching `name`, and had a description beginning `Use when`. Every mentioned `references/*.md` file existed, and neither skill contained TODO, TBD, or PLACEHOLDER. Recursive root skill count was exactly two.

| Backplane skill | SHA-256 | References | Result |
|---|---|---:|---|
| `managing-superpowers-backlog` | `739A16FCDF2EE5ADAB0514F5A44DB0629DCCE558985FE5A31D71DD2606AC1E81` | 3 | PASS |
| `managing-superpowers-handoffs` | `A6052755128BE9C7D268D71241DD389B9BF1C720834E47E61CBF9535F4CA92DE` | 2 | PASS |

The four required upstream `SKILL.md` files existed in the independent checkout and the native installed cache. Each pair had the same SHA-256:

| Upstream skill | SHA-256 | Result |
|---|---|---|
| `using-superpowers` | `82C5C8866AD7F5DD4440CE66BD7806BA48A2F13771BEAE5CF112E53F08FE36BA` | PASS |
| `brainstorming` | `A32D2255354775AA124855AA7100CF276BEA096FFF4EBB3A0EDF57BE216E6C72` | PASS |
| `writing-plans` | `0BC3D36590F7B2C323ED3EC18FF77E9F8ED57AF42F5680A02B11A2D20DE265CF` | PASS |
| `writing-skills` | `BBDFE742F853562E643A3D40D64476359D47881E39CEF80A189283FA26D11AB9` | PASS |

**Score:** `skill-structure` PASS. This is a file-structure check; it does not claim native plugin discovery in a fresh agent session.

## Task 4 correction recheck

After the canonical-path and dirty-adoption reference edits, a fresh PowerShell structure check again found exactly two canonical skills, valid frontmatter, all five direct references, no placeholders, both canonical root paths, and the separate dirty adoption/update rule. The corrected installation reference SHA-256 is 50D82CCACBF71D368E983984157ABE91D1FAFD977F1F4D654C0FD58B5393329D. The first ad hoc assertion failed because its regex did not span a Markdown line break; the corrected assertion passed. That assertion failure did not indicate a source defect.
