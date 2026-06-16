class Task:
    """Represents a task."""

    task_count = 0

    def __init__(self, title, assigned_to, status="Pending"):
        self.title = title
        self.assigned_to = assigned_to
        self._status = status
        Task.task_count += 1

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        if value in ["Pending", "Completed"]:
            self._status = value

    def __str__(self):
        return f"{self.title} - {self.status}"