"""Module provides database settings."""

DATABASE_PATH = "database.sqlite"

DATABASE_STRUCTURE = {
    "users": ["id", "name", "surname"],
    "tasks": ["id", "name", "description"],
    "users_tasks": ["id", "user_id", "task_id"],
}
