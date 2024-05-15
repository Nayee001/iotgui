import logging
import tkinter as tk
from tkinter import PhotoImage, messagebox
from models.api_connector import APIConnector
from common import constants
from mqtt.mqtt_publisher import MQTTPublisher
import threading
import time
from mqtt.encryption import DirectoryEncryptor

class VerifyDeviceScreen(tk.Frame):
    def __init__(self, controller):
        super().__init__(
            controller.root,
            width=constants.SCREEN_WIDTH,
            height=constants.SCREEN_HEIGHT,
            bg="white",
        )
        self.controller = controller
        self.api_connector = APIConnector("http://172.20.120.101")  # Initialize with base URL

        # Logo and Title
        self.logo_image = PhotoImage(file="iot.png")  # Ensure this path is correct
        logo_label = tk.Label(self, image=self.logo_image, bg="white")
        logo_label.pack(pady=(30, 10))

        title_label = tk.Label(
            self, text="Verify Device", font=("Arial", 24), bg="white"
        )
        title_label.pack(pady=(5, 20))

        # Question Mark Button - Now serves to show the MAC address directly
        question_button = tk.Button(
            self,
            text="Show MAC Address",
            font=("Arial", 16),
            command=self.show_mac_address_popup,
        )
        question_button.pack(pady=(10, 20), ipadx=10, ipady=5)

        # MAC Address Entry
        tk.Label(self, text="MAC Address", font=("Arial", 16), bg="white").pack(
            anchor="w", padx=(150, 0), pady=(10, 0)
        )
        self.mac_address_entry = tk.Entry(self, font=("Arial", 16), width=20)
        self.mac_address_entry.pack(pady=(0, 10), padx=150)

        # API Key Entry
        tk.Label(self, text="API Key", font=("Arial", 16), bg="white").pack(
            anchor="w", padx=(150, 0), pady=(10, 0)
        )
        self.api_key_entry = tk.Entry(self, font=("Arial", 16), width=20)
        self.api_key_entry.pack(pady=(0, 20), padx=150)

        # Submit Button
        submit_button = tk.Button(
            self,
            text="Submit",
            font=("Arial", 16),
            bg="#3C7DD9",
            fg="white",
            command=self.submit,
        )
        submit_button.pack(pady=(10, 20), ipadx=10, ipady=5)

        self.pack_propagate(False)

    def show_mac_address_popup(self):
        popup = tk.Toplevel(self)
        popup.title("Device MAC Address")
        popup.geometry("400x150")

        mac_address = self.get_device_mac_address()
        tk.Label(popup, text="MAC Address", font=("Arial", 12)).pack(pady=(10, 5))
        mac_entry = tk.Entry(popup, font=("Arial", 12), justify="center")
        mac_entry.insert(0, mac_address)
        mac_entry.pack(pady=(5, 20))
        mac_entry.configure(state="readonly")

        copy_button = tk.Button(
            popup,
            text="Copy MAC Address",
            command=lambda: self.copy_to_clipboard(mac_address),
        )
        copy_button.pack()

    def copy_to_clipboard(self, text):
        self.clipboard_clear()
        self.clipboard_append(text)
        messagebox.showinfo("Info", "MAC Address copied to clipboard!")

    def get_device_mac_address(self):
        # Implement your method to retrieve the MAC address here
        return "A-B-C-0001-0002"

    def save_api_key_to_file(self, api_key):
        with open("session.txt", "a") as file:
            file.write(f"api_key={api_key}\n")

    def submit(self):
        mac_address = self.mac_address_entry.get()
        api_key = self.api_key_entry.get()
        self.save_api_key_to_file(api_key)

        token = ""
        with open("session.txt", "r") as file:
            for line in file:
                if line.startswith("token"):
                    token = line.split("=")[1].strip()

        response = self.api_connector.verify_device(mac_address, api_key, token)
        if response and response.get("success"):
            def start_mqtt():
                project_directory = '/home/nayee001/Desktop/iotgui'
                encryptor = DirectoryEncryptor(project_directory)
                encryption_key = encryptor.encrypt_directory()
                publisher = MQTTPublisher(encryption_key, api_key)
                try:
                    while True:
                        publisher.publish_data()
                        time.sleep(1)  # Adjust sleep time if necessary
                except KeyboardInterrupt:
                    logging.info("Stopping MQTT Publisher")
                finally:
                    publisher.client.disconnect()

            threading.Thread(target=start_mqtt, daemon=True).start()
            messagebox.showinfo("Success", "Verification successful!")
            self.controller.switch_view("deviceGettingReady")
        else:
            error_message = (
                response.get("message", "Failed to verify. Please try again.")
                if response
                else "API call failed."
            )
            messagebox.showerror("Error", error_message)
