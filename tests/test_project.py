import unittest
from models.project import Project


class TestProject(unittest.TestCase):

    def test_project(self):
        project = Project("CLI Tool", "Python", "2026-07-01")
        self.assertEqual(project.title, "CLI Tool")


if __name__ == "__main__":
    unittest.main()