import unittest
from models.user import User


class TestUser(unittest.TestCase):

    def test_user(self):
        user = User("Alex", "alex@gmail.com")
        self.assertEqual(user.name, "Alex")


if __name__ == "__main__":
    unittest.main()