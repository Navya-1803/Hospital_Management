import tkinter as tk
from tkinter import messagebox
from models import surgery

def show_surgeries():
    win = tk.Toplevel()
    win.title("Surgery Records")

    data = surgery.fetch_surgeries()

    tk.Label(win, text="Surgery_ID | Patient_ID | Surgeon_ID | Date | Details").pack()
    for row in data:
        tk.Label(win, text=str(row)).pack()

def add_surgery():
    win = tk.Toplevel()
    win.title("Add Surgery")

    entries = []
    labels = ["Surgery ID", "Patient ID", "Surgeon ID", "Date", "Details"]
    for i, lbl in enumerate(labels):
        tk.Label(win, text=lbl).grid(row=i, column=0)
        e = tk.Entry(win)
        e.grid(row=i, column=1)
        entries.append(e)

    def submit():
        values = [e.get() for e in entries]
        try:
            surgery.insert_surgery(*values)
            messagebox.showinfo("Success", "Surgery Added!")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(win, text="Add Surgery", command=submit).grid(row=len(labels), columnspan=2)

def delete_surgery():
    win = tk.Toplevel()
    win.title("Delete Surgery")

    tk.Label(win, text="Enter Surgery ID to Delete:").grid(row=0, column=0)
    entry = tk.Entry(win)
    entry.grid(row=0, column=1)

    def submit():
        surgery_id = entry.get()
        try:
            surgery.delete_surgery(surgery_id)
            messagebox.showinfo("Success", f"Surgery ID {surgery_id} deleted!")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(win, text="Delete Surgery", command=submit).grid(row=1, columnspan=2)

def surgery_gui(root):
    frame = tk.LabelFrame(root, text="Surgery Module", padx=10, pady=10)
    frame.pack(padx=10, pady=10)

    tk.Button(frame, text="View Surgeries", command=show_surgeries).pack(side="left", padx=5)
    tk.Button(frame, text="Add Surgery", command=add_surgery).pack(side="left", padx=5)
    tk.Button(frame, text="Delete Surgery", command=delete_surgery).pack(side="left", padx=5)
