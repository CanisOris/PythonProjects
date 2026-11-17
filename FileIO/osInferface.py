
# modules
import os

"""
'r'        open for reading (default)
'w'        open for writing, truncating the file first
'x'        create a new file and open it for writing
'a'        open for writing, appending to the end of the file if it exists
'b'        binary mode
't'        text mode (default)
'+'        open a disk file for updating (reading and writing)
'U'        universal newline mode (deprecated)
"""
directory = "PythonProjects"
subfolder = "FileIO"
filename = "test.txt"

# r acts like @ in c# for raw string literals
# path = r"C:\Users\CanisOris\PythonProjects\FileIO\test.txt"


def startup():
    print("Starting up the OS interface module.")
    full_path = os.path.join(directory, subfolder, filename)
    print(f"Full path to the file: {full_path}")
    if os.path.exists(full_path):
        print("The file exists.")
    else:
        print("The file does not exist.")
    






if __name__ == "__main__":
    startup()