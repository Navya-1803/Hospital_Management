import tkinter as tk
from tkinter import messagebox
from models import patient

def show_patients():
    win = tk.Toplevel()
    win.title("Patient Records")

    data = patient.fetch_patients()

    tk.Label(win, text="Patient_ID | Patient_Name | D_O_B | Age | PhoneNo | RoomNo").pack()
    for row in data:
        tk.Label(win, text=str(row)).pack()

def add_patient():
    win = tk.Toplevel()
    win.title("Add Patient")

    entries = []
    labels = ["Patient ID", "Patient Name", "Date of Birth (YYYY-MM-DD)", "Age", "Phone No", "Room No"]
    for i, lbl in enumerate(labels):
        tk.Label(win, text=lbl).grid(row=i, column=0)
        e = tk.Entry(win)
        e.grid(row=i, column=1)
        entries.append(e)

    def submit():
        values = [e.get() for e in entries]
        try:
            patient.insert_patient(*values)
            messagebox.showinfo("Success", "Patient Added!")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(win, text="Add Patient", command=submit).grid(row=len(labels), columnspan=2)

def delete_patient():
    win = tk.Toplevel()
    win.title("Delete Patient")

    tk.Label(win, text="Enter Patient ID to Delete:").grid(row=0, column=0)
    entry = tk.Entry(win)
    entry.grid(row=0, column=1)

    def submit():
        patient_id = entry.get()
        try:
            patient.delete_patient(patient_id)
            messagebox.showinfo("Success", f"Patient ID {patient_id} deleted!")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(win, text="Delete Patient", command=submit).grid(row=1, columnspan=2)

def patient_gui(root):
    frame = tk.LabelFrame(root, text="Patient Module", padx=10, pady=10)
    frame.pack(padx=10, pady=10)

    tk.Button(frame, text="View Patients", command=show_patients).pack(side="left", padx=5)
    tk.Button(frame, text="Add Patient", command=add_patient).pack(side="left", padx=5)
    tk.Button(frame, text="Delete Patient", command=delete_patient).pack(side="left", padx=5)
