import tkinter as tk
import tkinter.filedialog as tk_fd


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





if __name__ == "__main__":
    root = tk.Tk()
    app = ParentWindow(master=root)
    app.pack(fill="both", expand=True)
    root.mainloop()