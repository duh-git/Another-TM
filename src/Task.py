"""Task Class"""

from random import randint


class Task:
    """Main Class"""

    def __init__(self, name: str, description: str, status: str = "Undone", id: int = None):
        self.name: str = name
        self.description: str = description
        self.status: str = status
        self.id: int = id if id is not None else self.generate_id()

    def generate_id(self, start: int = 10**5, end: int = 10**6) -> int:
        """Generates random number in range [start, end)."""
        return randint(start, end - 1)

    def __str__(self):
        formatted_id = f"{self.id:^6}"
        formatted_name = f"{self.name:^24}" if len(self.name) < 24 else f"{self.name:.21}..."
        formatted_status = f"{self.status:^16}" if len(self.status) < 16 else f"{self.status:.13}..."
        formatted_description = (
            f"{self.description:^32}" if len(self.description) < 32 else f"{self.description:.29}..."
        )
        return f"| {formatted_id} | {formatted_name} | {formatted_status} | {formatted_description} |"


if __name__ == "__main__":
    task0 = Task("Task 0", "Do something very stupid cuz i can")
    tasks = [Task(f"Task {i+1}", "Testing task for test only") for i in range(5)]

    print(task0)
    print(*(task for task in tasks), sep="\n")

    task_for_serching_or_deleting = tasks[2]  # Search by id, without using enumerate
    print(
        "\nFind task by list id (not by task.id) index",
        tasks.index(task_for_serching_or_deleting),
    )
