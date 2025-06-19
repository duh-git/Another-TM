"""
Module generating light database for app.
"""

if __name__ == "__main__":
    from functions import (
        create_table,
        delete_table,
        get_existing_tables,
        get_registered_tables,
        get_unregistered_tables,
    )

    for table in get_registered_tables():
        create_table(table)

    for table in get_unregistered_tables():
        delete_table(table)
        print(f"Deleted unregistered table: {table}")

    print("Tables:\t", ", ".join(get_existing_tables()))
