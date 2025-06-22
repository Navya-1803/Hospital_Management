import tkinter as tk
from tkinter import messagebox
from models import medical_record

def show_medical_records():
    win = tk.Toplevel()
    win.title("Medical Record Records")

    data = medical_record.fetch_medical_records()

    tk.Label(win, text="Record_ID | Patient_ID | Disease | Treatment | Date").pack()
    for row in data:
        tk.Label(win, text=str(row)).pack()

def add_medical_record():
    win = tk.Toplevel()
    win.title("Add Medical Record")

    entries = []
    labels = ["Record ID", "Patient ID", "Disease", "Treatment", "Date"]
    for i, lbl in enumerate(labels):
        tk.Label(win, text=lbl).grid(row=i, column=0)
        e = tk.Entry(win)
        e.grid(row=i, column=1)
        entries.append(e)

    def submit():
        values = [e.get() for e in entries]
        try:
            medical_record.insert_medical_record(*values)
            messagebox.showinfo("Success", "Medical Record Added!")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(win, text="Add Medical Record", command=submit).grid(row=len(labels), columnspan=2)

def delete_medical_record():
    win = tk.Toplevel()
    win.title("Delete Medical Record")

    tk.Label(win, text="Enter Record ID to Delete:").grid(row=0, column=0)
    entry = tk.Entry(win)
    entry.grid(row=0, column=1)

    def submit():
        record_id = entry.get()
        try:
            medical_record.delete_medical_record(record_id)
            messagebox.showinfo("Success", f"Record ID {record_id} deleted!")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(win, text="Delete Medical Record", command=submit).grid(row=1, columnspan=2)

def medical_record_gui(root):
    frame = tk.LabelFrame(root, text="Medical Record Module", padx=10, pady=10)
    frame.pack(padx=10, pady=10)

    tk.Button(frame, text="View Medical Records", command=show_medical_records).pack(side="left", padx=5)
    tk.Button(frame, text="Add Medical Record", command=add_medical_record).pack(side="left", padx=5)
    tk.Button(frame, text="Delete Medical Record", command=delete_medical_record).pack(side="left", padx=5)
