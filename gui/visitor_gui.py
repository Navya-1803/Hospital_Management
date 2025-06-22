import tkinter as tk
from tkinter import messagebox
from models import visitor

def show_visitors():
    win = tk.Toplevel()
    win.title("Visitor Records")

    data = visitor.fetch_visitors()

    tk.Label(win, text="Visitor_ID | Name | Contact | Purpose | Patient_ID").pack()
    for row in data:
        tk.Label(win, text=str(row)).pack()

def add_visitor():
    win = tk.Toplevel()
    win.title("Add Visitor")

    entries = []
    labels = ["Visitor ID", "Name", "Contact", "Purpose", "Patient ID"]
    for i, lbl in enumerate(labels):
        tk.Label(win, text=lbl).grid(row=i, column=0)
        e = tk.Entry(win)
        e.grid(row=i, column=1)
        entries.append(e)

    def submit():
        values = [e.get() for e in entries]
        try:
            visitor.insert_visitor(*values)
            messagebox.showinfo("Success", "Visitor Added!")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(win, text="Add Visitor", command=submit).grid(row=len(labels), columnspan=2)

def delete_visitor():
    win = tk.Toplevel()
    win.title("Delete Visitor")

    tk.Label(win, text="Enter Visitor ID to Delete:").grid(row=0, column=0)
    entry = tk.Entry(win)
    entry.grid(row=0, column=1)

    def submit():
        visitor_id = entry.get()
        try:
            visitor.delete_visitor(visitor_id)
            messagebox.showinfo("Success", f"Visitor ID {visitor_id} deleted!")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(win, text="Delete Visitor", command=submit).grid(row=1, columnspan=2)

def visitor_gui(root):
    frame = tk.LabelFrame(root, text="Visitor Module", padx=10, pady=10)
    frame.pack(padx=10, pady=10)

    tk.Button(frame, text="View Visitors", command=show_visitors).pack(side="left", padx=5)
    tk.Button(frame, text="Add Visitor", command=add_visitor).pack(side="left", padx=5)
    tk.Button(frame, text="Delete Visitor", command=delete_visitor).pack(side="left", padx=5)
