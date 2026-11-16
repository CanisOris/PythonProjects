
import io
import os

# print(dir(str))
# print(help(io))
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
target_dir = os.path.join(os.getcwd(), "PythonProjects", "FileIO")
target_filepath = os.path.join(target_dir, "test.txt")

 
def writeData():
    try:
        with open(target_filepath, "a", encoding="utf-8") as file:
            file.write("This is a test.")
            
            print("File written successfully.")
    except FileNotFoundError as e:
        # This catches both if the directory doesn't exist OR if  missing
        print(f"Error: {e}")
    except NotADirectoryError:
        print(f"Error: '{target_dir}' is not a directory.")
    except PermissionError:
        print(f"Error: Permission denied to access the path.")



def openFile():
  
    
    try:
        print(f"Current working directory: {os.getcwd()}")
        os.chdir(target_dir)
        print(f"Changed directory to: {os.getcwd()}")
        
        # try open
        with open(target_filepath, "r", encoding="utf-8") as file:
            content = file.read()
            print(content)
            print("File read successfully.")

    except FileNotFoundError as e:
        # This catches both if the directory doesn't exist OR if  missing
        print(f"Error: {e}")
    except NotADirectoryError:
        print(f"Error: '{target_dir}' is not a directory.")
    except PermissionError:
        print(f"Error: Permission denied to access the path.")


# print(os.listdir())

# print(os.path.abspath(os.getcwd()))
# print(os.path.dirname(os.path.abspath(os.getcwd())))
# print(os.path.basename(os.path.abspath(os.getcwd())))
# print(os.path.join(os.path.dirname(os.path.abspath(os.getcwd())), os.path.basename(os.path.abspath(os.getcwd()))))


if __name__ == "__main__":
    writeData()
    openFile()
