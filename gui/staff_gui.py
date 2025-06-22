import tkinter as tk
from tkinter import messagebox
from models import staff

def show_staff():
    win = tk.Toplevel()
    win.title("Staff Records")

    data = staff.fetch_staff()

    tk.Label(win, text="Staff_ID | Staff_Name | Staff_Role | Dept_ID").pack()
    for row in data:
        tk.Label(win, text=str(row)).pack()

def add_staff():
    win = tk.Toplevel()
    win.title("Add Staff")

    entries = []
    labels = ["Staff ID", "Staff Name", "Staff Role", "Dept ID"]
    for i, lbl in enumerate(labels):
        tk.Label(win, text=lbl).grid(row=i, column=0)
        e = tk.Entry(win)
        e.grid(row=i, column=1)
        entries.append(e)

    def submit():
        values = [e.get() for e in entries]
        try:
            staff.insert_staff(*values)
            messagebox.showinfo("Success", "Staff Added!")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(win, text="Add Staff", command=submit).grid(row=len(labels), columnspan=2)

def delete_staff():
    win = tk.Toplevel()
    win.title("Delete Staff")

    tk.Label(win, text="Enter Staff ID to Delete:").grid(row=0, column=0)
    entry = tk.Entry(win)
    entry.grid(row=0, column=1)

    def submit():
        staff_id = entry.get()
        try:
            staff.delete_staff(staff_id)
            messagebox.showinfo("Success", f"Staff ID {staff_id} deleted!")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(win, text="Delete Staff", command=submit).grid(row=1, columnspan=2)

def staff_gui(root):
    frame = tk.LabelFrame(root, text="Staff Module", padx=10, pady=10)
    frame.pack(padx=10, pady=10)

    tk.Button(frame, text="View Staff", command=show_staff).pack(side="left", padx=5)
    tk.Button(frame, text="Add Staff", command=add_staff).pack(side="left", padx=5)
    tk.Button(frame, text="Delete Staff", command=delete_staff).pack(side="left", padx=5)
