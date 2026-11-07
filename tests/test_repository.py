"""Check shipped skill resources and documentation through their public boundaries."""

import json
import re
import shutil
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ShippedResourcesTests(unittest.TestCase):
    """Catch unusable skill references, native metadata drift and invalid guide code."""

    def test_canonical_skill_identities(self):
        """Reject an absent or renamed canonical skill entry point."""
        for name in ("managing-superpowers-backlog", "managing-superpowers-handoffs"):
            with self.subTest(skill=name):
                body = (ROOT / "skills" / name / "SKILL.md").read_text(encoding="utf-8")
                self.assertTrue(body.startswith("---\n"))
                frontmatter = body.split("---", 2)[1]
                self.assertRegex(frontmatter, rf"(?m)^name: {re.escape(name)}$")
                self.assertRegex(frontmatter, r"(?m)^description: Use when ")

    def test_local_skill_references_exist(self):
        """Reject a package whose canonical instructions link missing resources."""
        documents = sorted((ROOT / "skills").rglob("*.md"))
        self.assertTrue(documents)
        for document in documents:
            for target in re.findall(r"\]\(([^)]+)\)", document.read_text(encoding="utf-8")):
                if target.startswith(("https://", "http://", "#")):
                    continue
                with self.subTest(document=str(document.relative_to(ROOT)), target=target):
                    self.assertTrue((document.parent / target.split("#", 1)[0]).is_file())

    def test_native_product_versions_agree(self):
        """Reject native host packages advertising conflicting product identities."""
        paths = ("package.json", "plugin.json", ".claude-plugin/plugin.json")
        identities = []
        for path in paths:
            manifest = json.loads((ROOT / path).read_text(encoding="utf-8"))
            identities.append((manifest["name"], manifest["version"]))
        self.assertEqual(len(set(identities)), 1)
        market = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text(encoding="utf-8"))
        self.assertEqual(
            (market["plugins"][0]["name"], market["plugins"][0]["version"]), identities[0]
        )

    def test_python_guide_examples_compile(self):
        """Catch syntax errors in documented Python before users execute the guides."""
        count = 0
        for guide in sorted((ROOT / "docs").glob("installing-*.md")):
            body = guide.read_text(encoding="utf-8")
            for number, code in enumerate(re.findall(r"(?ms)^```python\n(.*?)^```", body), 1):
                with self.subTest(guide=guide.name, block=number):
                    compile(code, f"{guide.name}:python-block-{number}", "exec")
                count += 1
        self.assertGreater(count, 0, "guide discovery found no Python examples")

    def test_python_guide_examples_pass_ruff(self):
        """Reject guide lint/format defects without executing native example operations."""
        executable = shutil.which("ruff")
        if executable is None:
            self.fail("Ruff is required from the locked development environment")
        for guide in sorted((ROOT / "docs").glob("installing-*.md")):
            blocks = re.findall(r"(?ms)^```python\n(.*?)^```", guide.read_text(encoding="utf-8"))
            if not blocks:
                continue
            for arguments in (("check",), ("format", "--check")):
                with self.subTest(guide=guide.name, arguments=arguments):
                    result = subprocess.run(
                        [executable, *arguments, "--stdin-filename", "guide.py", "-"],
                        input="\n".join(blocks),
                        cwd=ROOT,
                        capture_output=True,
                        text=True,
                        encoding="utf-8",
                        check=False,
                    )
                    self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
