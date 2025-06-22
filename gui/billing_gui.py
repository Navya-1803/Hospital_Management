import tkinter as tk
from tkinter import messagebox
from models import billing

def show_billings():
    win = tk.Toplevel()
    win.title("Billing Records")

    data = billing.fetch_billings()

    tk.Label(win, text="Billing_ID | Patient_ID | Amount | Date").pack()
    for row in data:
        tk.Label(win, text=str(row)).pack()

def add_billing():
    win = tk.Toplevel()
    win.title("Add Billing")

    entries = []
    labels = ["Billing ID", "Patient ID", "Amount", "Date"]
    for i, lbl in enumerate(labels):
        tk.Label(win, text=lbl).grid(row=i, column=0)
        e = tk.Entry(win)
        e.grid(row=i, column=1)
        entries.append(e)

    def submit():
        values = [e.get() for e in entries]
        try:
            billing.insert_billing(*values)
            messagebox.showinfo("Success", "Billing Added!")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(win, text="Add Billing", command=submit).grid(row=len(labels), columnspan=2)

def delete_billing():
    win = tk.Toplevel()
    win.title("Delete Billing")

    tk.Label(win, text="Enter Billing ID to Delete:").grid(row=0, column=0)
    entry = tk.Entry(win)
    entry.grid(row=0, column=1)

    def submit():
        billing_id = entry.get()
        try:
            billing.delete_billing(billing_id)
            messagebox.showinfo("Success", f"Billing ID {billing_id} deleted!")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(win, text="Delete Billing", command=submit).grid(row=1, columnspan=2)

def update_billing():
    win = tk.Toplevel()
    win.title("Update Billing")

    entries = []
    labels = ["Billing ID", "New Patient ID", "New Amount", "New Date"]
    for i, lbl in enumerate(labels):
        tk.Label(win, text=lbl).grid(row=i, column=0)
        e = tk.Entry(win)
        e.grid(row=i, column=1)
        entries.append(e)

    def submit():
        values = [e.get() for e in entries]
        try:
            billing.update_billing(*values)
            messagebox.showinfo("Success", f"Billing ID {values[0]} updated!")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(win, text="Update Billing", command=submit).grid(row=len(labels), columnspan=2)

def billing_gui(root):
    frame = tk.LabelFrame(root, text="Billing Module", padx=10, pady=10)
    frame.pack(padx=10, pady=10)

    tk.Button(frame, text="View Billings", command=show_billings).pack(side="left", padx=5)
    tk.Button(frame, text="Add Billing", command=add_billing).pack(side="left", padx=5)
    tk.Button(frame, text="Delete Billing", command=delete_billing).pack(side="left", padx=5)
    tk.Button(frame, text="Update Billing", command=update_billing).pack(side="left", padx=5)
