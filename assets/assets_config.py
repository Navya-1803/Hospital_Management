# assets/assets_config.py

# Color Scheme
PRIMARY_COLOR = "#0078D7"  # Blue
SECONDARY_COLOR = "#E5E5E5"  # Light Gray
TEXT_COLOR = "#333333"  # Dark Text

# Fonts
HEADER_FONT = ("Helvetica", 16, "bold")
LABEL_FONT = ("Helvetica", 12)
BUTTON_FONT = ("Helvetica", 10, "bold")

# Padding and spacing
PADDING = 10
GAP = 5

# Common messages
SUCCESS_ADD = "Record added successfully!"
SUCCESS_DELETE = "Record deleted successfully!"
ERROR_MSG = "Something went wrong. Please try again."

# Common function: clear all entries
def clear_entries(entry_list):
    """Clears all entries in a given list of entry widgets."""
    for entry in entry_list:
        entry.delete(0, 'end')
