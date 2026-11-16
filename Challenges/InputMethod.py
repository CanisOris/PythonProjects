import os
import re

file_name = input("Enter the file name: ").strip()
# todo: limit input to safe directory and sanitize further

try:
    # remove any unwanted characters from the file name
    if not re.match(r"^[\w\-. ]+$", file_name):
        print("Error: File name contains invalid characters.")
    
    # narrow down to .json files only
    elif not file_name.lower().endswith(".json"):
        print("Error: Only .json files are allowed.")
        
    else:
        # if the file exists, notify the user
        if os.path.exists(file_name):
            print("The specified JSON file exists.")
        else:
            print("That file name does not exist.")

except Exception as e:
    print(f"Error processing path: {e}")