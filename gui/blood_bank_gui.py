import tkinter as tk
from tkinter import messagebox
from models import blood_bank

def show_blood_banks():
    win = tk.Toplevel()
    win.title("Blood Bank Records")

    data = blood_bank.fetch_blood_banks()

    tk.Label(win, text="Blood_ID | Patient_ID | Blood_Type | Availability | Donor_name").pack()
    for row in data:
        tk.Label(win, text=str(row)).pack()

def add_blood_bank():
    win = tk.Toplevel()
    win.title("Add Blood Bank")

    entries = []
    labels = ["Blood ID", "Patient ID", "Blood Type", "Availability", "Donor Name"]
    for i, lbl in enumerate(labels):
        tk.Label(win, text=lbl).grid(row=i, column=0)
        e = tk.Entry(win)
        e.grid(row=i, column=1)
        entries.append(e)

    def submit():
        values = [e.get() for e in entries]
        try:
            blood_bank.insert_blood_bank(*values)
            messagebox.showinfo("Success", "Blood Bank Entry Added!")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(win, text="Add Blood Bank", command=submit).grid(row=len(labels), columnspan=2)

def delete_blood_bank():
    win = tk.Toplevel()
    win.title("Delete Blood Bank Entry")

    tk.Label(win, text="Enter Blood ID to Delete:").grid(row=0, column=0)
    entry = tk.Entry(win)
    entry.grid(row=0, column=1)

    def submit():
        blood_id = entry.get()
        try:
            blood_bank.delete_blood_bank(blood_id)
            messagebox.showinfo("Success", f"Blood ID {blood_id} deleted!")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(win, text="Delete Blood Bank", command=submit).grid(row=1, columnspan=2)

def blood_bank_gui(root):
    frame = tk.LabelFrame(root, text="Blood Bank Module", padx=10, pady=10)
    frame.pack(padx=10, pady=10)

    tk.Button(frame, text="View Blood Banks", command=show_blood_banks).pack(side="left", padx=5)
    tk.Button(frame, text="Add Blood Bank", command=add_blood_bank).pack(side="left", padx=5)
    tk.Button(frame, text="Delete Blood Bank", command=delete_blood_bank).pack(side="left", padx=5)
