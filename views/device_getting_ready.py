import logging
import tkinter as tk
from tkinter import messagebox
from common import constants
import threading
import paho.mqtt.client as paho
import json
import os

# MQTT configuration
from mqtt.mqtt_credentials import broker_address, client_name, port, user, password

class DeviceGettingReadyScreen(tk.Frame):
    def __init__(self, controller):
        super().__init__(controller.root, width=constants.SCREEN_WIDTH, height=constants.SCREEN_HEIGHT, bg='white')
        self.controller = controller

        # UI elements
        message_label = tk.Label(
            self,
            text="Please Check Command Center or Emails\nAccept your device from your command center\nPlease do not power off the device during this process.",
            font=("Arial", 14),
            bg='white',
            justify=tk.CENTER,
            padx=20
        )
        message_label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        self.api_key = self.get_api_key()
        if not self.api_key:
            messagebox.showerror("Error", "API key not found. Please ensure the session file is correct.")
            return

        self.mqtt_topic = f"mqttdevice/{self.api_key}"

        # Set up MQTT subscriber
        self.mqtt_client = paho.Client(client_name)
        self.mqtt_client.username_pw_set(user, password)
        self.mqtt_client.on_connect = self.on_connect
        self.mqtt_client.on_message = self.on_message
        self.mqtt_client.connect(broker_address, port, 60)

        threading.Thread(target=self.mqtt_client.loop_forever, daemon=True).start()

    def get_api_key(self):
        try:
            if os.path.exists("session.json"):
                with open("session.json", "r") as file:
                    data = json.load(file)
                    return data.get("api_key", None)
            else:
                logging.error("session.json not found.")
                return None
        except Exception as e:
            logging.error(f"Error reading API key from file: {e}")
            return None

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            logging.info("Connected to MQTT Broker!")
            print('Connected to MQTT Broker!')
            print(self.mqtt_topic)
            client.subscribe(self.mqtt_topic)
        else:
            logging.error(f"Failed to connect, return code {rc}\n")

    def on_message(self, client, userdata, msg):
        message = msg.payload.decode()
        print("Received message")
        print(message)
        logging.info(f"Received message: {message}")

        try:
            data = json.loads(message)
            keys_of_interest = ["status", "device", "location", "timestamp"]

            for key in keys_of_interest:
                if key in data:
                    self.save_response_to_file(key, data[key])
                    if key == "status" and data[key].lower() == "verified":
                        messagebox.showinfo("Device Accepted", "The device is Accepted.")
                    self.proceed_to_dashboard()
                
        except json.JSONDecodeError as e:
            logging.error(f"Error decoding JSON: {e}")

    def save_response_to_file(self, key, response):
        try:
            # Read the current contents of the file
            data = {}
            if os.path.exists("session.json"):
                with open("session.json", "r") as file:
                    data = json.load(file)

            # Update the key-value pair
            data[key] = response

            # Write the updated contents back to the file
            with open("session.json", "w") as file:
                json.dump(data, file, indent=4)

            logging.info(f"{key} saved successfully.")

        except Exception as e:
            logging.error(f"Error saving {key} to file: {e}")
            messagebox.showerror("Error", f"Failed to save {key} to file.")

    def proceed_to_dashboard(self):
        self.controller.switch_view('deviceDashboard')

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Device Getting Ready")
    controller = type('Controller', (object,), {'root': root})
    app = DeviceGettingReadyScreen(controller)
    app.pack(fill='both', expand=True)
    root.mainloop()
