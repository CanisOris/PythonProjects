import sqlite3
import os
from contextlib import contextmanager

TARGET_FOLDER = os.path.join(os.getcwd(), "PythonProjects", "SqlConn")
database = os.path.join(TARGET_FOLDER, "SubmissionAssignment.db")
conn = sqlite3.connect(database)

# file list tuple
fileList = ('information.docx','Hello.txt','myImage.png','myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')
#what endts with .txt create a new list
matched_files = [file for file in fileList if file.endswith('.txt')]
print(matched_files)

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
    """
    conn = sqlite3.connect(db_file)
    try:
        # still trying to understand generator behavior with context managers
        # The yield statement allows the connection to be used within the context block.
        # Once the block is exited, the code in the finally clause ensures the connection is closed.
        yield conn
    finally:
        # Guaranteed to run, even if queries raise an exception
        conn.close()  

# lazy evaluation vs eager evaluation
# i woul have split the filename and extension before inserting them into the database
# os.path.splitext(file_name)


try:
    with create_connection(database) as conn:
        cursor = conn.cursor()

        # 2 fields: ID and file_name
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tbl_files (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                file_name TEXT NOT NULL
            )
        """)

#         try:
#     with create_connection(database) as conn:
#         cursor = conn.cursor()
#         cursor.execute("CREATE TABLE IF NOT EXISTS tbl_files ( \
#             ID INTEGER PRIMARY KEY AUTOINCREMENT, \
#             name, \
#             ext \
#         )")
#         conn.commit()
#         for file_name in matched_files:
#             cursor.execute("INSERT INTO tbl_files(name, ext) VALUES (?,?)", ([0], os.path.splitext(file_name)[1]))
#             conn.commit()
        
#         cursor.execute("SELECT * FROM tbl_files")
#         print(cursor.fetchall())

# except sqlite3.Error as e:

        print(f"Database error: {e}")

        rows_to_insert = [(file_name,) for file_name in matched_files]
        cursor.executemany(
            "INSERT INTO tbl_files (file_name) VALUES (?)",
            rows_to_insert,
        )
        conn.commit()

        cursor.execute("SELECT ID, file_name FROM tbl_files")
        records = cursor.fetchall()

        print("Qualifying .txt files in database:")
        for row_id, stored_name in records:
            print(f"  [{row_id}] {stored_name}")

except sqlite3.Error as e:
    print(f"Database error: {e}")



