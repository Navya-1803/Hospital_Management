import tkinter as tk
from tkinter import messagebox
from models import emergency

def show_emergencies():
    win = tk.Toplevel()
    win.title("Emergency Records")

    data = emergency.fetch_emergencies()

    tk.Label(win, text="Case_ID | Patient_ID | Date | Details | PhoneNo").pack()
    for row in data:
        tk.Label(win, text=str(row)).pack()

def add_emergency():
    win = tk.Toplevel()
    win.title("Add Emergency")

    entries = []
    labels = ["Case ID", "Patient ID", "Date", "Details", "Phone No"]
    for i, lbl in enumerate(labels):
        tk.Label(win, text=lbl).grid(row=i, column=0)
        e = tk.Entry(win)
        e.grid(row=i, column=1)
        entries.append(e)

    def submit():
        values = [e.get() for e in entries]
        try:
            emergency.insert_emergency(*values)
            messagebox.showinfo("Success", "Emergency Added!")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(win, text="Add Emergency", command=submit).grid(row=len(labels), columnspan=2)

def delete_emergency():
    win = tk.Toplevel()
    win.title("Delete Emergency")

    tk.Label(win, text="Enter Case ID to Delete:").grid(row=0, column=0)
    entry = tk.Entry(win)
    entry.grid(row=0, column=1)

    def submit():
        cid = entry.get()
        try:
            emergency.delete_emergency(cid)
            messagebox.showinfo("Success", f"Emergency Case ID {cid} deleted!")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(win, text="Delete Emergency", command=submit).grid(row=1, columnspan=2)

def emergency_gui(root):
    frame = tk.LabelFrame(root, text="Emergency Module", padx=10, pady=10)
    frame.pack(padx=10, pady=10)

    tk.Button(frame, text="View Emergencies", command=show_emergencies).pack(side="left", padx=5)
    tk.Button(frame, text="Add Emergency", command=add_emergency).pack(side="left", padx=5)
    tk.Button(frame, text="Delete Emergency", command=delete_emergency).pack(side="left", padx=5)
