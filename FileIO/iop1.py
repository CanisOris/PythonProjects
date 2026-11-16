
import io
import os

# print(dir(str))
# print(help(io))
 
try:
    target_dir = os.getcwd() + os.sep + "PythonProjects" + os.sep + "FileIO"
    print(os.getcwd())
    os.chdir(target_dir)
    print(os.getcwd())
    with open("test.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"Error: The directory '{target_dir}' does not exist.")
except NotADirectoryError:
    print(f"Error: '{target_dir}' is not a directory.")
except PermissionError:
    print(f"Error: Permission denied to access '{target_dir}'.")


# print(os.listdir())

# print(os.path.abspath(os.getcwd()))
# print(os.path.dirname(os.path.abspath(os.getcwd())))
# print(os.path.basename(os.path.abspath(os.getcwd())))
# print(os.path.join(os.path.dirname(os.path.abspath(os.getcwd())), os.path.basename(os.path.abspath(os.getcwd()))))



