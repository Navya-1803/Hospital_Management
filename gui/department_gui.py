import tkinter as tk
from tkinter import messagebox
from models import department

def show_departments():
    win = tk.Toplevel()
    win.title("Department Records")

    data = department.fetch_departments()

    tk.Label(win, text="Dept_ID | Dept_Name").pack()
    for row in data:
        tk.Label(win, text=str(row)).pack()

def add_department():
    win = tk.Toplevel()
    win.title("Add Department")

    entries = []
    labels = ["Dept ID", "Dept Name"]
    for i, lbl in enumerate(labels):
        tk.Label(win, text=lbl).grid(row=i, column=0)
        e = tk.Entry(win)
        e.grid(row=i, column=1)
        entries.append(e)

    def submit():
        values = [e.get() for e in entries]
        try:
            department.insert_department(*values)
            messagebox.showinfo("Success", "Department Added!")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(win, text="Add Department", command=submit).grid(row=len(labels), columnspan=2)

def delete_department():
    win = tk.Toplevel()
    win.title("Delete Department")

    tk.Label(win, text="Enter Dept ID to Delete:").grid(row=0, column=0)
    entry = tk.Entry(win)
    entry.grid(row=0, column=1)

    def submit():
        dept_id = entry.get()
        try:
            department.delete_department(dept_id)
            messagebox.showinfo("Success", f"Dept ID {dept_id} deleted!")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(win, text="Delete Department", command=submit).grid(row=1, columnspan=2)

def department_gui(root):
    frame = tk.LabelFrame(root, text="Department Module", padx=10, pady=10)
    frame.pack(padx=10, pady=10)

    tk.Button(frame, text="View Departments", command=show_departments).pack(side="left", padx=5)
    tk.Button(frame, text="Add Department", command=add_department).pack(side="left", padx=5)
    tk.Button(frame, text="Delete Department", command=delete_department).pack(side="left", padx=5)
