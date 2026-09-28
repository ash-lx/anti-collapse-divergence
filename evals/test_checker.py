"""Public CLI regression checks, including documented semantic blind spots.

These assert honest triage behavior, not general semantic accuracy.
Run from the skill root: python3 -m unittest discover -s evals -p 'test_*.py' -v
"""

import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "check_frame_collisions.py"
FIXTURES = ROOT / "evals" / "fixtures"


class CheckerContractTests(unittest.TestCase):
    def run_checker(self, path, *args):
        return subprocess.run(
            [sys.executable, str(SCRIPT), str(path), *args],
            capture_output=True,
            text=True,
            check=False,
        )

    def check_fixture(self, name, expected_status, expected_candidates):
        process = self.run_checker(FIXTURES / (name + ".json"))
        self.assertEqual(process.returncode, expected_status, process.stderr)
        result = json.loads(process.stdout)
        self.assertIs(result["candidate_clusters_found"], expected_candidates)
        self.assertIs(result["collisions_found"], expected_candidates)
        self.assertFalse(result["certifies_collisions"])
        self.assertFalse(result["certifies_distinctness"])
        for cluster in result["clusters"]:
            self.assertTrue(cluster["review_needed"])
            self.assertIsNone(cluster["repair_needed"])
        if expected_candidates:
            self.assertEqual(result["verdict"], "review_flagged_candidates")
            self.assertTrue(result["clusters"])
        else:
            self.assertEqual(result["clusters"], [])
            self.assertEqual(
                result["verdict"],
                "no_clusters_detected_by_heuristic_only_not_a_pass",
            )
        return result

    def test_detected_overlap_requires_review(self):
        self.check_fixture("attestation-collapse", 1, True)

    def test_basic_diverse_set_gets_no_certificate(self):
        self.check_fixture("diverse-basic", 0, False)

    def test_known_paraphrased_duplicate_is_missed_without_certification(self):
        # The receiving party's token requirement is the same mechanism in
        # both frames. This fixture documents a lexical false negative.
        self.check_fixture("lexicon-blind-collapse", 0, False)

    def test_shared_fields_do_not_authorize_repair(self):
        # Insufficient money and completed work are distinct causal hypotheses,
        # although actor, renewal trigger, and subscription carrier match.
        result = self.check_fixture("distinct-renewal-causes", 1, True)
        self.assertEqual(
            set(result["clusters"][0]["frames"]),
            {"Cash shortage", "Job completed"},
        )

    def test_markdown_keeps_review_contract(self):
        process = self.run_checker(
            FIXTURES / "distinct-renewal-causes.json", "--markdown"
        )
        self.assertEqual(process.returncode, 1, process.stderr)
        self.assertIn("Candidate clusters found: **true**", process.stdout)
        self.assertIn("Certifies collisions: **false**", process.stdout)
        self.assertIn("Certifies distinctness: **false**", process.stdout)
        self.assertIn("not automatic repair", process.stdout)
        self.assertIn("Cash shortage", process.stdout)
        self.assertIn("Job completed", process.stdout)

    def test_invalid_json_and_wrong_shapes_exit_two(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "input.json"
            for text in ("{", "{}", '["not a frame"]'):
                with self.subTest(input=text):
                    path.write_text(text, encoding="utf-8")
                    process = self.run_checker(path)
                    self.assertEqual(process.returncode, 2)
                    self.assertTrue(process.stderr)
                    self.assertEqual(process.stdout, "")


if __name__ == "__main__":
    unittest.main()
