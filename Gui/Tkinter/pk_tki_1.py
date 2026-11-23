import tkinter
from tkinter import *


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        self.master = master
        self.master.title("Tkinter GUI")
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(700, 500))
        self.master.configure(bg="#2F5EB4")


        self.varFName = StringVar()
        self.varLName = StringVar()

        # self.varFName.set("Boob")
        # self.varLName.set("Roobertson")
        
        # print(self.varFName.get())
        # print(self.varLName.get())

        

        self.lblFName = Label(self.master, text='First Name: ', \
                            borderwidth=0, \
                            relief="solid", \
                            padx=5, pady=10, \
                            anchor="w", \
                            justify="left", \
                            wraplength=200, \
                            width=10, height=1, \
                            font=("Arial", 14), \
                            fg="white", \
                            bg="#2F5EB4")
        self.entFName = Entry(self.master, textvariable=self.varFName, \
                            borderwidth=2, \
                            relief="solid", \
                            font=("Arial", 14), \
                            fg="white", \
                            bg="#2F5EB4")
        self.lblLName = Label(self.master, text='Last Name: ', \
                            borderwidth=0, \
                            relief="solid", \
                            padx=5, pady=10, \
                            anchor="w", \
                            justify="left", \
                            wraplength=200, \
                            width=10, height=1, \
                            font=("Arial", 14), \
                            fg="white", \
                            bg="#2F5EB4")
        self.entLName = Entry(self.master, textvariable=self.varLName, \
                            borderwidth=2, \
                            relief="solid", \
                            font=("Arial", 14), \
                            fg="white", \
                            bg="#2F5EB4")
        self.btnSubmit = Button(self.master, text="Submit", \
                            width=12, \
                            height=1, \
                            font=("Arial", 16), \
                            fg="gold", \
                            bg="#182063")
        self.btnSubmit.bind("<Button-1>", self.submit)
        self.btnCancel = Button(self.master, text="Cancel", \
                            width=12, \
                            height=1, \
                            font=("Arial", 16), \
                            fg="gold", \
                            bg="#182063")
        self.btnCancel.bind("<Button-1>", self.cancel)  

        self.lblbDisplay = Label(self.master, text="", \
                                borderwidth=0, \
                                relief="solid", \
                                padx=5, pady=10, \
                                anchor="w", \
                                justify="left", \
                                wraplength=200, \
                                width=10, height=1, \
                                font=("Arial", 14), \
                                fg="white", \
                                bg="#2F5EB4")
        
        
        # grid geometry manager
        self.lblFName.grid(row=0, column=0)
        self.entFName.grid(row=0, column=1, padx=10, pady=10)
        self.lblLName.grid(row=1, column=0)
        self.entLName.grid(row=1, column=1, padx=10, pady=10)
        self.btnSubmit.grid(row=2, column=1, padx=10, pady=(30, 0), sticky="ew")
        self.btnCancel.grid(row=2, column=0, padx=10, pady=(30, 0), sticky="ew")
        self.lblbDisplay.grid(row=3, column=0, columnspan=2)
        


        
    def submit(self, event):
        print(self.varFName.get())
        print(self.varLName.get())
        # config method updates the label text
        self.lblbDisplay.config(text=f"{self.varFName.get()} {self.varLName.get()}")

    def cancel(self, event):
        self.master.destroy()

if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
    