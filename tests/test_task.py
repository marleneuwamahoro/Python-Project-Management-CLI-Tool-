import unittest
from models.task import Task


class TestTask(unittest.TestCase):

    def test_task_status(self):
        task = Task("Coding", "Alex")
        task.status = "Completed"

        self.assertEqual(task.status, "Completed")


if __name__ == "__main__":
    unittest.main()