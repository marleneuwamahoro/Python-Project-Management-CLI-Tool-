from models.person import Person


class User(Person):
    """Represents a user."""

    user_count = 0

    def __init__(self, name, email):
        super().__init__(name)
        self.email = email
        User.user_count += 1

    def __str__(self):
        return f"{self.name} ({self.email})"