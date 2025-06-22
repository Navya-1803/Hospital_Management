import tkinter as tk
from tkinter import messagebox
from models import insurance

def show_insurances():
    win = tk.Toplevel()
    win.title("Insurance Records")

    data = insurance.fetch_insurances()

    tk.Label(win, text="Policy_ID | Patient_ID | Provider | Coverage_Amount").pack()
    for row in data:
        tk.Label(win, text=str(row)).pack()

def add_insurance():
    win = tk.Toplevel()
    win.title("Add Insurance")

    entries = []
    labels = ["Policy ID", "Patient ID", "Provider", "Coverage Amount"]
    for i, lbl in enumerate(labels):
        tk.Label(win, text=lbl).grid(row=i, column=0)
        e = tk.Entry(win)
        e.grid(row=i, column=1)
        entries.append(e)

    def submit():
        values = [e.get() for e in entries]
        try:
            insurance.insert_insurance(*values)
            messagebox.showinfo("Success", "Insurance Added!")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(win, text="Add Insurance", command=submit).grid(row=len(labels), columnspan=2)

def delete_insurance():
    win = tk.Toplevel()
    win.title("Delete Insurance")

    tk.Label(win, text="Enter Policy ID to Delete:").grid(row=0, column=0)
    entry = tk.Entry(win)
    entry.grid(row=0, column=1)

    def submit():
        policy_id = entry.get()
        try:
            insurance.delete_insurance(policy_id)
            messagebox.showinfo("Success", f"Policy ID {policy_id} deleted!")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(win, text="Delete Insurance", command=submit).grid(row=1, columnspan=2)

def insurance_gui(root):
    frame = tk.LabelFrame(root, text="Insurance Module", padx=10, pady=10)
    frame.pack(padx=10, pady=10)

    tk.Button(frame, text="View Insurances", command=show_insurances).pack(side="left", padx=5)
    tk.Button(frame, text="Add Insurance", command=add_insurance).pack(side="left", padx=5)
    tk.Button(frame, text="Delete Insurance", command=delete_insurance).pack(side="left", padx=5)
