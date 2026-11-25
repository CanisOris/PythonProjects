import tkinter as tk
from tkinter import *
import webbrowser
import os

# use same path based on this files path.
TARGET_FOLDER = os.path.dirname(os.path.abspath(__file__))
TARGET_FILE = os.path.join(TARGET_FOLDER, "index.html")


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.varOut = tk.StringVar()
        self.master.title("Web Page Generator")
        self.master.geometry("800x170")
        self.master.minsize(650, 170)
        self.master.configure(bg="#2F5EB4")

        # expand to fill the available width and height.
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(2, weight=1)
        # Label prompting the user to enter custom text or use the default page.
        self.lblFName = Label(
            self.master,
            text="Enter custom text or click the Default HTML Page button",
            anchor="w",
            font=("Segoe UI", 9),
            fg="black",
            bg="#f0f0f0"
        )
        self.lblFName.grid(
            row=0, column=0, columnspan=3,
            sticky="ew", padx=(22, 16), pady=(20, 10)
        )
        # Entry field for custom text.
        self.custTxt = Entry(
            self.master,
            textvariable=self.varOut,
            font=("Segoe UI", 9),
            fg="black",
            bg="white",
            relief="sunken",
            borderwidth=2
        )
        self.custTxt.grid(
            row=1, column=0, columnspan=3,
            sticky="ew", padx=(28, 16)
        )
        # Button to generate the default HTML page.
        self.btn = Button(
            self.master,
            text="Default HTML Page",
            width=28,
            height=2,
            font=("Segoe UI", 9),
            command=self.defaultHTML
        )
        self.btn.grid(
            row=2, column=1, sticky="se", padx=(0, 18), pady=(18, 10)
        )
        # Button to submit custom text.
        self.btn2 = Button(
            self.master,
            text="Submit Custom Text",
            width=28,
            height=2,
            font=("Segoe UI", 9),
            command=self.submitCustomText
        )
        self.btn2.grid(
            row=2, column=2, sticky="se", padx=(0, 12), pady=(18, 10)
        )
    # Write the custom text to an HTML file and open it in a new browser tab.
    def submitCustomText(self):
        htmlText = self.varOut.get()
        htmlFile = open(TARGET_FILE, "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab(TARGET_FILE)


    # Write the default HTML page to a file and open it in a new browser tab.
    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open(TARGET_FILE, "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab(TARGET_FILE)





if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()