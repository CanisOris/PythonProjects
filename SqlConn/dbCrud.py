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
        with sqlite3.connect(db_file) as conn:
            return conn
    except sqlite3.Error as e:
        print(f"Error: {e}")
    return None



if __name__ == "__main__":

    TARGET_FOLDER = os.path.join(os.getcwd(), "PythonProjects", "SqlConn")
    database = os.path.join(TARGET_FOLDER, "test.db")
    conn = create_connection(database)
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_persons ( \
                    ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                    col_fname TEXT, \
                    col_lname TEXT, \
                    col_email TEXT \
                    )")
        cur.close()
    