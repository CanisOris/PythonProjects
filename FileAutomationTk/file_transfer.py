import tkinter as tk
import tkinter.filedialog as tk_fd
import tkinter.messagebox as tk_mb
import os
import shutil
import time

TARGET_SOURCE = os.path.join(os.getcwd(), "PythonProjects", "FileAutomationTk","Customer_Source")
TARGET_DEST = os.path.join(os.getcwd(), "PythonProjects", "FileAutomationTk","Customer_Destination")

class ParentWindow(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master.title("File Transfer")
        self.master.resizable(width=False, height=False)
        self.master.geometry("858x600")
        self.configure(bg="#2F5EB4")

        self.sourceDir_btn = tk.Button(self, text="Select Source", width=20)
        self.sourceDir_btn.grid(row=0, column=0, padx=(20, 10), pady=(30, 0))

        self.source_dir = tk.Entry(self, width=54, font=("Arial", 14))
        self.source_dir.grid(row=0, column=1, columnspan=2, padx=(10, 20), pady=(30, 0))

        self.destDir_btn = tk.Button(self, text="Select Destination", width=20, command=self.destDir)
        self.destDir_btn.grid(row=1, column=0, padx=(20, 10), pady=(15, 0))

        self.dest_dir = tk.Entry(self, width=54, font=("Arial", 14))
        self.dest_dir.grid(row=1, column=1, columnspan=2, padx=(10, 20), pady=(15, 0))

        self.sourceDir_btn = tk.Button(self, text="Select Source", width=20, command=self.sourceDir)
        self.sourceDir_btn.grid(row=0, column=0, padx=(20, 10), pady=(30, 0))

        self.destDir_btn = tk.Button(self, text="Select Destination", width=20, command=self.destDir)
        self.destDir_btn.grid(row=1, column=0, padx=(20, 10), pady=(15, 0))

        self.include_new = tk.BooleanVar(master=self, value=False)
        self.include_updated = tk.BooleanVar(master=self, value=True)
        filters = tk.Frame(self, bg="#2F5EB4")
        filters.grid(row=2, column=1, columnspan=2, sticky="w", padx=(10, 20), pady=(15, 0))
        self.new_checkbox = tk.Checkbutton(
            filters, text="New (created in the last 24 hours)",
            variable=self.include_new, bg="#2F5EB4"
        )
        self.new_checkbox.grid(row=0, column=0, sticky="w")
        self.updated_checkbox = tk.Checkbutton(
            filters, text="Updated (modified in the last 24 hours)",
            variable=self.include_updated, bg="#2F5EB4"
        )
        self.updated_checkbox.grid(row=1, column=0, sticky="w")

        # transfer button
        self.transfer_btn = tk.Button(self, text="Transfer Files", width=20, command=self.transferFiles)
        self.transfer_btn.grid(row=3, column=1, padx=(200, 0), pady=(20, 15))

        #Creates an Exit button
        self.exit_btn = tk.Button(self, text="Exit", width=20, command=self.exit_program)
        #Positions the Exit button
        self.exit_btn.grid(row=3, column=2, padx=(10, 40), pady=(20, 15))

        self.source_dir.insert(0, TARGET_SOURCE)
        self.dest_dir.insert(0, TARGET_DEST)
    
    #Creates function to select source directory.
    def sourceDir(self):
        selectSourceDir = tk_fd.askdirectory()
        #The .delete(0, END) will clear the the content that is inserted in the Entry widget,
        #this allows the path to be inserted into the Entry widget properly.
        self.source_dir.delete(0, tk.END)
        #The .insert method will insert the user selection to the source_dir Entry
        self.source_dir.insert(0, selectSourceDir)

    def destDir(self):
        selectDestDir = tk_fd.askdirectory()
        #The .delete(0, END) will clear the the content that is inserted in the Entry widget,
        #this allows the path to be inserted into the Entry widget properly.
        self.dest_dir.delete(0, tk.END)
        #The .insert method will insert the user selection to the destination_dir Entry widget
        self.dest_dir.insert(0, selectDestDir)

    #Creates function to transfer files from one directory to another
    def transferFiles(self):
        include_new = self.include_new.get()
        include_updated = self.include_updated.get()
        if not (include_new or include_updated):
            tk_mb.showinfo("Select files", "Select New, Updated, or both before transferring.", parent=self.master)
            return
        #Gets source directory
        source = self.source_dir.get().strip()
        #Gets destination directory
        destination = self.dest_dir.get().strip()
        # Only transfer files created or modified within the last 24 hours.
        now = time.time()
        cutoff = now - (24 * 60 * 60)
        #Gets a list of files in the source directory
        source_files = os.listdir(source)
        #Runs through each file in the source directory
        for i in source_files:
            file_path = os.path.join(source, i)
            # Skip subfolders.
            if not os.path.isfile(file_path):
                continue
            # On Windows, getctime returns the file's creation time.
            created = os.path.getctime(file_path)
            modified = os.path.getmtime(file_path)
            if ((include_new and cutoff <= created <= now)
                    or (include_updated and cutoff <= modified <= now)):
                shutil.move(file_path, destination)
                print(i + ' was successfully transferred.')
          
        

    #Creates function to exit program
    def exit_program(self):
        #root is the main GUI window, the Tkinter destroy method
        #tells python to terminate root.mainloop and all widgets inside the GUI window
        root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ParentWindow(master=root)
    app.pack(fill="both", expand=True)
    root.mainloop()