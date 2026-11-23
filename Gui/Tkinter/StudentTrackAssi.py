import tkinter as tk
from tkinter import messagebox, ttk


class ParentWindow(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#2F5EB4", padx=20, pady=20)
        self.master.title("Student Tracking")
        self.master.geometry("944x562")
        self.master.minsize(650, 550)
        self.pack(fill="both", expand=True)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(8, weight=1)


        tk.Label(
            self, text="Student Tracking", font=("Arial", 22, "bold"),
            fg="white", bg="#2F5EB4"
        ).grid(row=0, column=0, columnspan=2, pady=(0, 20))

        self.varFName = tk.StringVar(self)
        self.varLName = tk.StringVar(self)
        self.varPhone = tk.StringVar(self)
        self.varEmail = tk.StringVar(self)
        self.varCourse = tk.StringVar(self)

        self.fields = [
            ("First name", self.varFName),
            ("Last name", self.varLName),
            ("Phone number", self.varPhone),
            ("Email", self.varEmail),
            ("Current course", self.varCourse),
        ]
        self.entries = []
        for row, (label, variable) in enumerate(self.fields, start=1):
            tk.Label(
                self, text=label + ":", font=("Arial", 12),
                fg="white", bg="#2F5EB4"
            ).grid(row=row, column=0, sticky="w", padx=(0, 12), pady=6)
            entry = tk.Entry(self, textvariable=variable, font=("Arial", 12))
            entry.grid(row=row, column=1, sticky="ew", pady=6)
            self.entries.append(entry)

        self.btnSubmit = tk.Button(
            self, text="Submit", command=self.submit,
            font=("Arial", 12), fg="gold", bg="#182063"
        )
        self.btnSubmit.grid(row=6, column=1, sticky="e", pady=(10, 20))


        # Title
        tk.Label(
            self, text="Students", font=("Arial", 16, "bold"),
            fg="white", bg="#2F5EB4"
        ).grid(row=7, column=0, columnspan=2, sticky="w", pady=(0, 8))

        # Table frame then iterate over the fields to create the table headings
        table_frame = tk.Frame(self)
        table_frame.grid(row=8, column=0, columnspan=2, sticky="nsew")
        table_frame.rowconfigure(0, weight=1)
        table_frame.columnconfigure(0, weight=1)

        columns = ("first_name", "last_name", "phone", "email", "course")

        self.student_list = ttk.Treeview(
            table_frame, columns=columns, show="headings", selectmode="extended"
        )
        for column, (label, _) in zip(columns, self.fields):
            self.student_list.heading(column, text=label)
            self.student_list.column(column, width=170, minwidth=120, anchor="w")
        self.student_list.grid(row=0, column=0, sticky="nsew")

        vertical_scroll = ttk.Scrollbar(
            table_frame, orient="vertical", command=self.student_list.yview
        )
        vertical_scroll.grid(row=0, column=1, sticky="ns")
        horizontal_scroll = ttk.Scrollbar(
            table_frame, orient="horizontal", command=self.student_list.xview
        )
        horizontal_scroll.grid(row=1, column=0, sticky="ew")
        self.student_list.configure(
            yscrollcommand=vertical_scroll.set,
            xscrollcommand=horizontal_scroll.set
        )

        self.btnDelete = tk.Button(
            self, text="Delete selected students", command=self.delete_students,
            font=("Arial", 12), fg="gold", bg="#C22C2C"
        )
        self.btnDelete.grid(row=9, column=0, columnspan=2, sticky="w", pady=(12, 0))
        self.entries[0].focus_set()



    def submit(self):
        values = [variable.get().strip() for _, variable in self.fields]
        if not all(values):
            messagebox.showwarning(
                "Missing information", "Please complete all five fields.",
                parent=self.master
            )
            return

        self.student_list.insert("", "end", values=values)
        for _, variable in self.fields:
            variable.set("")
        self.entries[0].focus_set()

    def delete_students(self):
        selected = self.student_list.selection()
        if selected:
            self.student_list.delete(*selected)


if __name__ == "__main__":
    root = tk.Tk()
    app = ParentWindow(root)
    root.mainloop()
