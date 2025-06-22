import tkinter as tk
from tkinter import messagebox
from models import user

def login():
    win = tk.Toplevel()
    win.title("Login")

    tk.Label(win, text="Username").grid(row=0, column=0)
    username_entry = tk.Entry(win)
    username_entry.grid(row=0, column=1)

    tk.Label(win, text="Password").grid(row=1, column=0)
    password_entry = tk.Entry(win, show="*")
    password_entry.grid(row=1, column=1)

    def submit():
        username = username_entry.get()
        password = password_entry.get()
        if user.authenticate_user(username, password):
            messagebox.showinfo("Success", "Login Successful!")
            win.destroy()
        else:
            messagebox.showerror("Error", "Invalid username or password!")

    tk.Button(win, text="Login", command=submit).grid(row=2, columnspan=2)

def auth_gui(root):
    frame = tk.LabelFrame(root, text="User Authentication", padx=10, pady=10)
    frame.pack(padx=10, pady=10)

    tk.Button(frame, text="Login", command=login).pack(side="left", padx=5)
