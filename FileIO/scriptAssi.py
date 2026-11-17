import os
import datetime

# Replace this with the absolute or relative path to your test folder

TARGET_FOLDER = os.path.join(os.getcwd(), "PythonProjects", "FileIO", "IOAssi")
# I know it was only for .txt but i like the idea of supporting multiple file types
ALLEXTENSIONS = ['.txt', '.md', '.csv', '.json']
EXTENSIONS = ALLEXTENSIONS[0]

def scan_text_files(folder_path):
    print(f"Scanning directory: {os.path.abspath(folder_path)}\n" + "-" * 60)
    
    # Verify the directory exists
    if not os.path.exists(folder_path):
        print(f"Error: Directory '{folder_path}' does not exist.")
        return

    txt_count = 0

    # Iterate through directory 
    for file_name in os.listdir(folder_path):
        
        # join path and file
        file_path = os.path.join(folder_path, file_name)
        
        # only get files with supported extensions
        if os.path.isfile(file_path) and any(file_name.lower().endswith(ext) for ext in EXTENSIONS):
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

    if txt_count == 0:
        print(f"No files ending with any of {EXTENSIONS} were found in this directory.")
    else:
        print(f"Successfully processed {txt_count} text file(s).")

if __name__ == "__main__":
    scan_text_files(TARGET_FOLDER)