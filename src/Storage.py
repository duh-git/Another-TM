from Task import Task
import json

class Storage:
  def __init__(self, db_path: str):
    self.db_path = db_path
    self.unserialyzed: str = json.load(open(db_path))
    self.serialyzed: list[Task] = self.serialyze()

  def serialyze(self) -> list[Task]:
    return [Task(**task) for task in self.unserialyzed["tasks"]]

  def store(self, name: str, description: str) -> None:
    task = Task(name, description)
    self.serialyzed.append(task)
    self.unserialyzed["tasks"].append(task.__dict__)
    json.dump(self.unserialyzed, f:=open(self.db_path, "w"), indent=2)

  def __str__(self):
    out = f"| {'ID':^6} | {'Name':^24} | {'Status':^16} | {'Description':^32} |\n"
    out += f"{'-' * (len(out) - 1)}\n"  # Crutch here, depends on your font
    for task in self.serialyzed:
      out += f"{task.__str__()}\n"
    return out

if __name__ == "__main__":
  storage = Storage("db.json")
  print(storage)
  