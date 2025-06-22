import tkinter as tk
from tkinter import messagebox
from models import pharmacy

def show_pharmacies():
    win = tk.Toplevel()
    win.title("Pharmacy Records")

    data = pharmacy.fetch_pharmacies()

    tk.Label(win, text="Medicine_ID | Name | Quantity | Price | Expiry_Date").pack()
    for row in data:
        tk.Label(win, text=str(row)).pack()

def add_pharmacy():
    win = tk.Toplevel()
    win.title("Add Pharmacy")

    entries = []
    labels = ["Medicine ID", "Name", "Quantity", "Price", "Expiry Date"]
    for i, lbl in enumerate(labels):
        tk.Label(win, text=lbl).grid(row=i, column=0)
        e = tk.Entry(win)
        e.grid(row=i, column=1)
        entries.append(e)

    def submit():
        values = [e.get() for e in entries]
        try:
            pharmacy.insert_pharmacy(*values)
            messagebox.showinfo("Success", "Pharmacy Added!")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(win, text="Add Pharmacy", command=submit).grid(row=len(labels), columnspan=2)

def delete_pharmacy():
    win = tk.Toplevel()
    win.title("Delete Pharmacy")

    tk.Label(win, text="Enter Medicine ID to Delete:").grid(row=0, column=0)
    entry = tk.Entry(win)
    entry.grid(row=0, column=1)

    def submit():
        medicine_id = entry.get()
        try:
            pharmacy.delete_pharmacy(medicine_id)
            messagebox.showinfo("Success", f"Medicine ID {medicine_id} deleted!")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(win, text="Delete Pharmacy", command=submit).grid(row=1, columnspan=2)

def pharmacy_gui(root):
    frame = tk.LabelFrame(root, text="Pharmacy Module", padx=10, pady=10)
    frame.pack(padx=10, pady=10)

    tk.Button(frame, text="View Pharmacies", command=show_pharmacies).pack(side="left", padx=5)
    tk.Button(frame, text="Add Pharmacy", command=add_pharmacy).pack(side="left", padx=5)
    tk.Button(frame, text="Delete Pharmacy", command=delete_pharmacy).pack(side="left", padx=5)
