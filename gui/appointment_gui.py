import tkinter as tk
from tkinter import messagebox
from models import appointment

def show_appointments():
    win = tk.Toplevel()
    win.title("Appointment Records")

    data = appointment.fetch_appointments()

    tk.Label(win, text="Appointment_ID | Patient_ID | Doctor_ID | Date | Time").pack()
    for row in data:
        tk.Label(win, text=str(row)).pack()

def add_appointment():
    win = tk.Toplevel()
    win.title("Add Appointment")

    entries = []
    labels = ["Appointment ID", "Patient ID", "Doctor ID", "Date (YYYY-MM-DD)", "Time (HH:MM)"]
    for i, lbl in enumerate(labels):
        tk.Label(win, text=lbl).grid(row=i, column=0)
        e = tk.Entry(win)
        e.grid(row=i, column=1)
        entries.append(e)

    def submit():
        values = [e.get() for e in entries]
        try:
            appointment.insert_appointment(*values)
            messagebox.showinfo("Success", "Appointment Added!")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(win, text="Add Appointment", command=submit).grid(row=len(labels), columnspan=2)

def delete_appointment():
    win = tk.Toplevel()
    win.title("Delete Appointment")

    tk.Label(win, text="Enter Appointment ID to Delete:").grid(row=0, column=0)
    entry = tk.Entry(win)
    entry.grid(row=0, column=1)

    def submit():
        appointment_id = entry.get()
        try:
            appointment.delete_appointment(appointment_id)
            messagebox.showinfo("Success", f"Appointment ID {appointment_id} deleted!")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(win, text="Delete Appointment", command=submit).grid(row=1, columnspan=2)

def update_appointment():
    win = tk.Toplevel()
    win.title("Update Appointment")

    entries = []
    labels = ["Appointment ID", "New Patient ID", "New Doctor ID", "New Date (YYYY-MM-DD)", "New Time (HH:MM)"]
    for i, lbl in enumerate(labels):
        tk.Label(win, text=lbl).grid(row=i, column=0)
        e = tk.Entry(win)
        e.grid(row=i, column=1)
        entries.append(e)

    def submit():
        values = [e.get() for e in entries]
        try:
            appointment.update_appointment(*values)
            messagebox.showinfo("Success", f"Appointment ID {values[0]} updated!")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(win, text="Update Appointment", command=submit).grid(row=len(labels), columnspan=2)

def appointment_gui(root):
    frame = tk.LabelFrame(root, text="Appointment Module", padx=10, pady=10)
    frame.pack(padx=10, pady=10)

    tk.Button(frame, text="View Appointments", command=show_appointments).pack(side="left", padx=5)
    tk.Button(frame, text="Add Appointment", command=add_appointment).pack(side="left", padx=5)
    tk.Button(frame, text="Delete Appointment", command=delete_appointment).pack(side="left", padx=5)
    tk.Button(frame, text="Update Appointment", command=update_appointment).pack(side="left", padx=5)
