import sqlite3
import os
from contextlib import contextmanager

TARGET_FOLDER = os.path.join(os.getcwd(), "PythonProjects", "SqlConn")
database = os.path.join(TARGET_FOLDER, "test2.db")
conn = sqlite3.connect(database)

'''
I ran into this issue before with another lang
A Python sqlite3 context manager gotcha
https://blog.rtwilson.com/a-python-sqlite3-context-manager-gotcha
/#:~:text=3%20Comments.%20Jonathan%20Ballet%20says%3A%20November%2016%2C,
the%20transaction%20is%20now%20up%20to%20you.

Looks like there is a solution
@contextmanager [decorator]
https://www.google.com/search?
q=python+%40contextmanager&
rlz=1C1OZZY_enUS1223US1223&
oq=python+%40contextmanager&
gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIGCAEQRRg60gEJMjg2OWowajE1qAIIsAIB
&sourceid=chrome
&source=chrome.rb
&ie=UTF-8

'''



# Test db connection get connection
@contextmanager
def create_connection(db_file):
    """
    Create a database connection to the SQLite database specified by db_file.
    Parameters:
    db_file (str): The database file path.
    Returns:Connection object or None if an error occurs.
    """
    conn = None

    try:
        conn = sqlite3.connect(db_file)
        try:
            yield conn
        finally:
            conn.close()
    except sqlite3.Error as e:
        print(f"Error: {e}")
        yield None
