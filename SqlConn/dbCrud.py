import sqlite3
import os

# print(sqlite3)


def create_connection(db_file):
    """
    Create a database connection to the SQLite database specified by db_file.

    Parameters:
    db_file (str): The database file path.

    Returns:
    Connection object or None if an error occurs.
    """
    conn = None

    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(f"Error: {e}")
    return conn 



if __name__ == "__main__":

    TARGET_FOLDER = os.path.join(os.getcwd(), "PythonProjects", "SqlConn")
    database = os.path.join(TARGET_FOLDER, "test.db")
    conn = create_connection(database)
    if conn:
        print("Connection successful")
        conn.close()
    else:
        print("Connection failed")