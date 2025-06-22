import tkinter as tk
from tkinter import messagebox
from models import room

def show_rooms():
    win = tk.Toplevel()
    win.title("Room Records")

    data = room.fetch_rooms()

    tk.Label(win, text="RoomNo | Room_Type | Patient_ID | Room_Status").pack()
    for row in data:
        tk.Label(win, text=str(row)).pack()

def add_room():
    win = tk.Toplevel()
    win.title("Add Room")

    entries = []
    labels = ["Room No", "Room Type", "Patient ID", "Room Status"]
    for i, lbl in enumerate(labels):
        tk.Label(win, text=lbl).grid(row=i, column=0)
        e = tk.Entry(win)
        e.grid(row=i, column=1)
        entries.append(e)

    def submit():
        values = [e.get() for e in entries]
        try:
            room.insert_room(*values)
            messagebox.showinfo("Success", "Room Added!")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(win, text="Add Room", command=submit).grid(row=len(labels), columnspan=2)

def delete_room():
    win = tk.Toplevel()
    win.title("Delete Room")

    tk.Label(win, text="Enter Room No to Delete:").grid(row=0, column=0)
    entry = tk.Entry(win)
    entry.grid(row=0, column=1)

    def submit():
        room_no = entry.get()
        try:
            room.delete_room(room_no)
            messagebox.showinfo("Success", f"Room No {room_no} deleted!")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(win, text="Delete Room", command=submit).grid(row=1, columnspan=2)

def room_gui(root):
    frame = tk.LabelFrame(root, text="Room Module", padx=10, pady=10)
    frame.pack(padx=10, pady=10)

    tk.Button(frame, text="View Rooms", command=show_rooms).pack(side="left", padx=5)
    tk.Button(frame, text="Add Room", command=add_room).pack(side="left", padx=5)
    tk.Button(frame, text="Delete Room", command=delete_room).pack(side="left", padx=5)
