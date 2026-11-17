import os
import datetime

# Replace this with the absolute or relative path to your test folder

TARGET_FOLDER = os.path.join(os.getcwd(), "PythonProjects", "FileIO", "IOAssi")
# I know it was only for .txt but i like the idea of supporting multiple file types
ALLEXTENSION = ['.txt', '.md', '.csv', '.json']
EXTENSION = ALLEXTENSION[0]

def scan_text_files(folder_path):
    '''
    Scans the specified folder for text files with the given extension.
    Prints the file name, full path, raw modification time, and human-readable modification time.

    Parameters:
    folder_path (str): The path to the folder to scan.
    '''
    txt_count = 0

    try:
        print(f"Scanning directory: {os.path.abspath(folder_path)}\n" + "-" * 60)
    
        # Verify the directory exists
        if not os.path.exists(folder_path):
            print(f"Error: Directory '{folder_path}' does not exist.")
            return

        # Iterate through directory 
        for file_name in os.listdir(folder_path):
            try:
                # join path and file
                file_path = os.path.join(folder_path, file_name)
                
                # only get files with supported EXTENSION
                if os.path.isfile(file_path) and any(file_name.lower().endswith(ext) for ext in EXTENSION):
                    txt_count += 1
                    
                    # get the timestamp
                    mtime_epoch = os.path.getmtime(file_path)
                    # seconds elapsed since the Unix Epoch (January 1, 1970, 00:00:00 UTC)
                    # so it needs conversion to a human-readable format
                    # Convert epoch time to a human-readable format for easier verification
                    mtime_readable = datetime.datetime.fromtimestamp(mtime_epoch).strftime('%Y-%m-%d %H:%M:%S')
                    
                    # Output Results
                    print(f"[{txt_count}] File Name : {file_name}")
                    print(f"    Full Path   : {file_path}")
                    print(f"    Raw mtime   : {mtime_epoch}")
                    print(f"    Modified    : {mtime_readable}")
                    # found this gem - you can multiply chars
                    print("-" * 60)
            # filnotfound, not a directory, or permission error in the inner loop
            except (FileNotFoundError, NotADirectoryError, PermissionError) as item:
                print(f"Error: {item}")
        if txt_count == 0:
            print(f"No files ending with any of {EXTENSION} were found in this directory.")
        else:
            print(f"Successfully processed {txt_count} text file(s).")
    # found cool compact way of catching multiple exceptions
    # filnotfound, not a directory, or permission error in the outer loop
    except (FileNotFoundError, NotADirectoryError, PermissionError) as outerLoop:
        print(f"Error: {outerLoop}")



if __name__ == "__main__":
    scan_text_files(TARGET_FOLDER)