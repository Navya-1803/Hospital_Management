import tkinter as tk
from tkinter import messagebox
from models import doctor

def show_doctors():
    win = tk.Toplevel()
    win.title("Doctor Records")

    data = doctor.fetch_doctors()

    tk.Label(win, text="Doctor_ID | Doctor_Name | Specialization | Dept_ID").pack()
    for row in data:
        tk.Label(win, text=str(row)).pack()

def add_doctor():
    win = tk.Toplevel()
    win.title("Add Doctor")

    entries = []
    labels = ["Doctor ID", "Doctor Name", "Specialization", "Dept ID"]
    for i, lbl in enumerate(labels):
        tk.Label(win, text=lbl).grid(row=i, column=0)
        e = tk.Entry(win)
        e.grid(row=i, column=1)
        entries.append(e)

    def submit():
        values = [e.get() for e in entries]
        try:
            doctor.insert_doctor(*values)
            messagebox.showinfo("Success", "Doctor Added!")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(win, text="Add Doctor", command=submit).grid(row=len(labels), columnspan=2)

def delete_doctor():
    win = tk.Toplevel()
    win.title("Delete Doctor")

    tk.Label(win, text="Enter Doctor ID to Delete:").grid(row=0, column=0)
    entry = tk.Entry(win)
    entry.grid(row=0, column=1)

    def submit():
        doctor_id = entry.get()
        try:
            doctor.delete_doctor(doctor_id)
            messagebox.showinfo("Success", f"Doctor ID {doctor_id} deleted!")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(win, text="Delete Doctor", command=submit).grid(row=1, columnspan=2)

def doctor_gui(root):
    frame = tk.LabelFrame(root, text="Doctor Module", padx=10, pady=10)
    frame.pack(padx=10, pady=10)

    tk.Button(frame, text="View Doctors", command=show_doctors).pack(side="left", padx=5)
    tk.Button(frame, text="Add Doctor", command=add_doctor).pack(side="left", padx=5)
    tk.Button(frame, text="Delete Doctor", command=delete_doctor).pack(side="left", padx=5)
