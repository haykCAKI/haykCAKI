import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
from check_confidential import check, word_hash  # noqa: E402

FIXTURES = Path(__file__).resolve().parent / "fixtures"

# A made-up client, so no real name has to live in the fixtures.
CONFIG = {"blocked_word_sha256": [word_hash("acmecorp")], "public_repos": ["haykCAKI", "boring.notch"]}


def run(fixture):
    return check((FIXTURES / fixture).read_text(encoding="utf-8"), CONFIG, fixture)


class CheckConfidential(unittest.TestCase):
    def test_clean_file_passes(self):
        self.assertEqual(run("clean.md"), [])

    def test_blocked_term_fails_naming_term_and_line(self):
        problems = run("client_name.md")
        self.assertEqual(len(problems), 1)
        self.assertIn("client_name.md:3", problems[0])
        self.assertIn("acmecorp", problems[0])

    def test_private_repo_link_fails(self):
        problems = run("private_repo.md")
        self.assertEqual(len(problems), 1)
        self.assertIn("secret_project", problems[0])


if __name__ == "__main__":
    unittest.main()
