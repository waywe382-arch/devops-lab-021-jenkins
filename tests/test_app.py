import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from app import get_status

class TestApplication(unittest.TestCase):

    def test_status_is_healthy(self):
        result = get_status()
        self.assertEqual(result["status"], "healthy")

    def test_application_name(self):
        result = get_status()
        self.assertEqual(
            result["application"],
            "lab-021-jenkins-demo"
        )

if __name__ == "__main__":
    unittest.main()
