import tkinter as tk
from tkinter import PhotoImage, messagebox
from common import constants
import threading
import paho.mqtt.client as paho
import logging
import json

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
            with open("session.txt", "r") as file:
                for line in file:
                    if line.startswith("api_key="):
                        return line.split("=")[1].strip()
        except FileNotFoundError:
            logging.error("session.txt not found.")
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
            if "status" in data:  # Replace "status" with the actual key you're looking for
                self.save_response_to_file(data["status"])
                self.proceed_to_dashboard()
        except json.JSONDecodeError as e:
            logging.error(f"Error decoding JSON: {e}")

    def save_response_to_file(self, response):
        try:
            # Read the current contents of the file
            with open("session.txt", "r") as file:
                lines = file.readlines()

            # Check if 'response' is present and update it
            response_present = False
            for i, line in enumerate(lines):
                if line.startswith("status="):  # Replace "status=" with the actual key
                    lines[i] = f"status={response}\n"  # Replace "status" with the actual key
                    response_present = True
                    break

            # If 'status' was not present, append it
            if not response_present:
                lines.append(f"status={response}\n")  # Replace "status" with the actual key

            # Write the updated contents back to the file
            with open("session.txt", "w") as file:
                file.writelines(lines)

            logging.info("Response saved successfully.")

        except FileNotFoundError:
            # If the file does not exist, create it and write the response
            with open("session.txt", "w") as file:
                file.write(f"status={response}\n")  # Replace "status" with the actual key
            logging.info("session.txt not found. Created new file and saved response.")

        except Exception as e:
            logging.error(f"Error saving response to file: {e}")
            messagebox.showerror("Error", " to save response to file.")

    def proceed_to_dashboard(self):
        self.controller.switch_view('deviceDashboard')