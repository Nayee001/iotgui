import tkinter as tk
from tkinter import PhotoImage, Toplevel, messagebox
from common import constants
import time
import threading

class VerifyDeviceScreen(tk.Frame):
    def __init__(self, controller):
        super().__init__(controller.root, width=constants.SCREEN_WIDTH, height=constants.SCREEN_HEIGHT, bg='white')
        self.controller = controller

        # Logo and Title
        self.logo_image = PhotoImage(file='iot.png')  # Ensure this path is correct
        logo_label = tk.Label(self, image=self.logo_image, bg='white')
        logo_label.pack(pady=(30, 10))
        title_label = tk.Label(self, text="Verify Device", font=("Arial", 24), bg='white')
        title_label.pack(pady=(5, 20))

        # Question Mark Button - Now serves to show the MAC address directly
        question_button = tk.Button(self, text="Show MAC Address", font=("Arial", 16), command=self.show_mac_address_popup)
        question_button.pack(pady=(10, 20), ipadx=10, ipady=5)

        # MAC Address Entry
        tk.Label(self, text="MAC Address", font=("Arial", 16), bg='white').pack(anchor='w', padx=(150, 0), pady=(10, 0))
        self.mac_address_entry = tk.Entry(self, font=("Arial", 16), width=20)
        self.mac_address_entry.pack(pady=(0, 10), padx=150)

        # API Key Entry
        tk.Label(self, text="API Key", font=("Arial", 16), bg='white').pack(anchor='w', padx=(150, 0), pady=(10, 0))
        self.api_key_entry = tk.Entry(self, font=("Arial", 16), width=20)
        self.api_key_entry.pack(pady=(0, 20), padx=150)

        # Submit Button
        submit_button = tk.Button(self, text="Submit", font=("Arial", 16), bg='#3C7DD9', fg='white', command=self.submit)
        submit_button.pack(pady=(10, 20), ipadx=10, ipady=5)

        self.pack_propagate(False)

    def show_mac_address_popup(self):
        self.popup = Toplevel(self)
        self.popup.title("Device MAC Address")
        self.popup.geometry("400x150")

        mac_address = self.get_device_mac_address()

        tk.Label(self.popup, text="MAC Address", font=("Arial", 12)).pack(pady=(10, 5))
        mac_entry = tk.Entry(self.popup, font=("Arial", 12), justify='center')
        mac_entry.insert(0, mac_address)
        mac_entry.pack(pady=(5, 20))
        mac_entry.configure(state='readonly')

        copy_button = tk.Button(self.popup, text="Copy MAC Address", command=lambda: self.copy_to_clipboard(mac_address))
        copy_button.pack()

    def copy_to_clipboard(self, text):
        self.clipboard_clear()
        self.clipboard_append(text)
        messagebox.showinfo("Info", "MAC Address copied to clipboard!")  # Changed to use messagebox for simplicity

    def get_device_mac_address(self):
        # Implement your method to retrieve the MAC address here
        return "00:1B:44:11:3A:B7"

    def submit(self):
        # Example validation
        mac_address = self.mac_address_entry.get()
        api_key = self.api_key_entry.get()
        if mac_address == "00:1B:44:11:3A:B7" and api_key == "4561AB":  # Replace with actual check
            messagebox.showinfo("Success", "Verification successful!")
            self.controller.switch_view('DeviceGettingReadyScreen')
        else:
            messagebox.showerror("Error", "Invalid MAC Address or API Key. Please try again.")

# Ensure your `controller` class is set up to handle the root window setup and switching views.
