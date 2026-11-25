import sqlite3
from contextlib import contextmanager
import os

TARGET_FOLDER = os.path.join(os.getcwd(), "PythonProjects", "sqliteTk")
database = os.path.join(TARGET_FOLDER, "test_database.db")
tbl1 = "tbl_files"
conn = sqlite3.connect(database)


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


insert_row = ("John", "Doe", 30)
try:
    with create_connection(database) as conn:
        cur = conn.cursor()

        cur.execute(f"DROP TABLE IF EXISTS {tbl1}")
        cur.execute(f"CREATE TABLE IF NOT EXISTS {tbl1} (FirstName TEXT, LastName TEXT, Age INT)")
        cur.execute(f"INSERT INTO {tbl1} (FirstName, LastName, Age) VALUES (?, ?, ?)", insert_row)
        conn.commit()

        insert_row = (insert_row, ("Jane", "Doe", 25))
        cur.executemany(f"INSERT INTO {tbl1} (FirstName, LastName, Age) VALUES (?, ?, ?)", insert_row)
        conn.commit()

        print("Records inserted successfully.")
        cur.execute(f"SELECT FirstName, LastName, Age FROM {tbl1}")
        records = cur.fetchall()
        for first_name, last_name, age in records:
            print(f"{first_name} {last_name}, Age: {age}")  

        # 
        # cursor.execute("""
        #     CREATE TABLE IF NOT EXISTS tbl_files (
        #         ID INTEGER PRIMARY KEY AUTOINCREMENT,
        #         file_name TEXT NOT NULL
        #     )
        # """)
        
        # loop and insert each matching filename into the database
        # rows_to_insert = [(file_name,) for file_name in matched_files]
        # cur.executemany(
        #     "INSERT INTO tbl_files (file_name) VALUES (?)",
        #     rows_to_insert,
        # )
        # conn.commit()

        cur.execute("SELECT ID, file_name FROM tbl_files")
        records = cur.fetchall()

        print("Qualifying .txt files in database:")
        for row_id, stored_name in records:
            print(f"  [{row_id}] {stored_name}")

    
except sqlite3.Error as e:
    print(f"Database error: {e}")





# TARGET_FOLDER = os.path.join(os.getcwd(), "PythonProjects", "sqliteTk")
# database = os.path.join(TARGET_FOLDER, "test_database.db")
# conn = sqlite3.connect(database)

# cur = conn.cursor()
# cur.execute("DROP TABLE IF EXISTS People")
# cur.execute("CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT)")
# """
# Instead of directly putting data into a SQL string—which leaves your database vulnerable 
# to SQL injection attacks—you use ? as placeholders and pass the actual values separately as a tuple.
# """

# insert_row = ("John", "Doe", 30)
# cur.execute("INSERT INTO People (FirstName, LastName, Age) VALUES (?, ?, ?)", insert_row)
# conn.commit()
# conn.close()
