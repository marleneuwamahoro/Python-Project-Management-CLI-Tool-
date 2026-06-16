class Project:
    """Represents a project."""

    project_count = 0

    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        Project.project_count += 1

    def __str__(self):
        return f"{self.title} - Due: {self.due_date}"