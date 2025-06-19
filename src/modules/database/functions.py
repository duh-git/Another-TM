"""Module providing functions for interacting with a database."""

import sqlite3
from settings import DATABASE_PATH, DATABASE_STRUCTURE


con = sqlite3.connect(DATABASE_PATH)
cur = con.cursor()


def get_existing_tables() -> list:
    """
    Get existing tables from database.

    :return: List of existing tables.
    """
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    con.commit()
    return list(table[0] for table in cur.fetchall())


def get_registered_tables() -> list:
    """
    Get registered tables from settings.

    :return: List of registered tables.
    """
    return list(DATABASE_STRUCTURE)


def get_unregistered_tables() -> list:
    """
    Get unregistered tables from database.

    :return: List of unregistered tables.
    """
    existing_tables = get_existing_tables()
    registered_tables = get_registered_tables()

    return list(table for table in existing_tables if table not in registered_tables)


def create_table(table_name: str, fields: list[str] = None) -> None:
    """Creating tables with fields.
    If it exists don't do anything.
    """
    try:
        cur.execute(
            f"CREATE TABLE {table_name} ({", ".join(DATABASE_STRUCTURE[table_name])});"
        )
        con.commit()

    except sqlite3.OperationalError:
        pass


def delete_table(table_name: str) -> None:
    """Deleting unregistered table.
    If it doesn't exists don't do anything.
    """
    cur.execute(f"DROP TABLE IF EXISTS {table_name};")
    con.commit()
