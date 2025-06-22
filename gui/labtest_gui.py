import tkinter as tk
from tkinter import messagebox
from models import labtest

def show_lab_tests():
    win = tk.Toplevel()
    win.title("Lab Test Records")

    data = labtest.fetch_lab_tests()

    tk.Label(win, text="TestName | Patient_ID | Doctor_ID | Result").pack()
    for row in data:
        tk.Label(win, text=str(row)).pack()

def add_lab_test():
    win = tk.Toplevel()
    win.title("Add Lab Test")

    entries = []
    labels = ["Test Name", "Patient ID", "Doctor ID", "Result"]
    for i, lbl in enumerate(labels):
        tk.Label(win, text=lbl).grid(row=i, column=0)
        e = tk.Entry(win)
        e.grid(row=i, column=1)
        entries.append(e)

    def submit():
        values = [e.get() for e in entries]
        try:
            labtest.insert_lab_test(*values)
            messagebox.showinfo("Success", "Lab Test Added!")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(win, text="Add Lab Test", command=submit).grid(row=len(labels), columnspan=2)

def delete_lab_test():
    win = tk.Toplevel()
    win.title("Delete Lab Test")

    tk.Label(win, text="Enter Test Name and Patient ID to Delete:").grid(row=0, column=0)
    test_entry = tk.Entry(win)
    test_entry.grid(row=0, column=1)
    patient_entry = tk.Entry(win)
    patient_entry.grid(row=0, column=2)

    def submit():
        test_name = test_entry.get()
        patient_id = patient_entry.get()
        try:
            labtest.delete_lab_test(test_name, patient_id)
            messagebox.showinfo("Success", f"Lab Test {test_name} for Patient {patient_id} deleted!")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(win, text="Delete Lab Test", command=submit).grid(row=1, columnspan=3)

def labtest_gui(root):
    frame = tk.LabelFrame(root, text="Lab Test Module", padx=10, pady=10)
    frame.pack(padx=10, pady=10)

    tk.Button(frame, text="View Lab Tests", command=show_lab_tests).pack(side="left", padx=5)
    tk.Button(frame, text="Add Lab Test", command=add_lab_test).pack(side="left", padx=5)
    tk.Button(frame, text="Delete Lab Test", command=delete_lab_test).pack(side="left", padx=5)
