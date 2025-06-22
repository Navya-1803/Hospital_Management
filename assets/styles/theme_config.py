import ttkbootstrap as tb
from ttkbootstrap.constants import *

def apply_theme():
    """Apply a pastel-themed design for the Hospital Management System."""
    
    # Set the theme (e.g., 'flatly', 'journal', 'minty', etc.)
    tb.Style().theme_use("minty")  # Minty theme has a soft, light background with pastel hues
    
    # Set custom pastel colors for buttons, labels, and entry fields
    style = tb.Style()
    
    # Pastel button styling
    style.configure("TButton", font=("Helvetica", 10, "bold"), padding=8, relief="flat", background="#a1c4fd", foreground="black")
    
    # Pastel label styling
    style.configure("TLabel", font=("Helvetica", 12), padding=5, background="#f7f7f7", foreground="#4f4f4f")
    
    # Pastel entry field style (light background with soft text)
    style.configure("TEntry", font=("Helvetica", 10), padding=5, fieldbackground="#f1f9fe", foreground="#555555")
    
    # Pastel background for frames
    style.configure("TFrame", background="#f7f7f7")
    
    # Scrollbar style with pastel colors
    style.configure("TScrollbar", gripcount=0, background="#a1c4fd", troughcolor="#f7f7f7", width=15)
    
    # Set a soft highlight for entry fields when focused
    style.map("TEntry", 
        foreground=[("focus", "#7bb6f3"), ("!focus", "#555555")],
        fieldbackground=[("focus", "#ffffff"), ("!focus", "#f1f9fe")])

    # Button hover effect (soft change in background color)
    style.map("TButton", 
        background=[("active", "#7bb6f3"), ("!active", "#a1c4fd")])

    # Apply the theme
    print("Pastel theme applied successfully.")

