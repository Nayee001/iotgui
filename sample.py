import tkinter as tk
from tkinter import messagebox

# Initialize the main window
root = tk.Tk()
root.title("vFCL Device Configuration")
root.geometry("800x480")  # Set size for Raspberry Pi touchscreen

# Set the font styles and colors
title_font = ("Helvetica", 18, "bold")
text_font = ("Helvetica", 12)
bg_color = "#FFFFFF"
text_color = "#4F4F4F"
highlight_color = "#3A73FF"

# Sample Functionality for Navigation (to be expanded)
def show_dashboard():
    # Clear the screen and display the dashboard
    for widget in root.winfo_children():
        widget.destroy()
    dashboard_screen()

def show_error():
    messagebox.showerror("Error", "An error has been encountered.")

def verify_device():
    # Verification logic here
    show_dashboard()

# Screens
def welcome_screen():
    welcome_label = tk.Label(root, text="Welcome to vFCL", font=title_font, fg=highlight_color, bg=bg_color)
    welcome_label.pack(expand=True)

def device_ready_screen():
    ready_label = tk.Label(root, text="Device is getting Ready ...", font=text_font, fg=text_color, bg=bg_color)
    ready_label.pack(expand=True)

def error_screen():
    error_label = tk.Label(root, text="Error encountered. Please contact support for assistance.", font=text_font, fg="#FFA500", bg=bg_color)
    error_label.pack(expand=True)

def verify_screen():
    verify_label = tk.Label(root, text="Verify Device", font=title_font, fg=highlight_color, bg=bg_color)
    verify_label.pack(pady=20)

    api_key_entry = tk.Entry(root, font=text_font, width=30)
    api_key_entry.pack(pady=10)

    verify_button = tk.Button(root, text="Verify", font=text_font, bg=highlight_color, fg="white", command=verify_device)
    verify_button.pack(pady=20)

def dashboard_screen():
    dashboard_label = tk.Label(root, text="vFCL Device 001", font=title_font, fg=highlight_color, bg=bg_color)
    dashboard_label.pack(pady=10)

    # More dashboard elements would go here

# Start with the welcome screen
welcome_screen()

root.mainloop()
