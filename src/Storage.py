"""Storage Class"""

import json
from Task import Task


class Storage:
    """Main Class"""

    def __init__(self, db_path: str):
        self.db_path = db_path
        self.unserialyzed: str = json.load(open(db_path))
        self.serialyzed: list[Task] = self.serialyze()

    def serialyze(self) -> list[Task]:
        """Parse Data"""
        return [Task(**task) for task in self.unserialyzed["tasks"]]

    def store(self, name: str, description: str) -> None:
        """Save changes"""
        task = Task(name, description)
        self.serialyzed.append(task)
        self.unserialyzed["tasks"].append(task.__dict__)
        with open(self.db_path, "w", encoding="UTF-8") as f:
            json.dump(self.unserialyzed, f, indent=2)

    def __str__(self):
        out = f"| {'ID':^6} | {'Name':^24} | {'Status':^16} | {'Description':^32} |\n"
        out += f"{'-' * (len(out) - 1)}\n"  # Crutch here, depends on your font
        for task in self.serialyzed:
            out += f"{task.__str__()}\n"
        return out


if __name__ == "__main__":
    storage = Storage("db.json")
    print(storage)
