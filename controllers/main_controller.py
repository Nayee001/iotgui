from views.welcome_screen import WelcomeScreen
from views.config_screen import ConfigScreen
from views.login_screen import LoginScreen
from views.verify_device_screen import VerifyDeviceScreen
from views.device_getting_ready import DeviceGettingReadyScreen
from views.device_dashboard import DeviceDashboardScreen
import re  # Import regular expressions
import logging
import json
import os

class MainController:
    def __init__(self, root):
        self.root = root
        self.views = {
            'welcome': WelcomeScreen(self),
            'config': ConfigScreen(self),
            'login': LoginScreen(self),  # Ensure the key is lowercase
            'verifyDevice': VerifyDeviceScreen(self),  # Ensure the key is correctly cased
            'deviceGettingReady': DeviceGettingReadyScreen(self),  # Ensure the key is correctly cased
            'deviceDashboard': DeviceDashboardScreen(self)  # Ensure the key is correctly cased
        }
        self.current_view = None
        self.initial_view = 'welcome'
        self.check_session_and_initialize()

    def switch_view(self, view_name):
        try:
            if self.current_view is not None:
                self.current_view.pack_forget()
            self.current_view = self.views[view_name]  # Access with the exact case
            self.current_view.pack()
            logging.info(f"Switched to view: {view_name}")
        except KeyError:
            logging.error(f"View '{view_name}' does not exist. Please check the dictionary keys.")
        except Exception as e:
            logging.error(f"An error occurred while switching views: {e}")

    def check_session_and_initialize(self):
        try:
            if os.path.exists('session.json'):
                with open('session.json', 'r') as file:
                    data = json.load(file)
                    logging.info("Session data read from file: %s", data)

                    session_active = data.get('session_active', False)
                    token_available = 'token' in data and bool(re.search(r'\d+\|[\w+]+', data['token']))
                    device_approved = data.get('status', '').lower() == 'verified'

                    if device_approved:
                        self.initial_view = 'deviceDashboard'  # Ensure this matches the dictionary key exactly
                    elif session_active and token_available:
                        self.initial_view = 'verifyDevice'  # Ensure this matches the dictionary key exactly
                    elif session_active:
                        self.initial_view = 'login'  # Ensure this matches the dictionary key exactly
                    else:
                        self.initial_view = 'welcome'  # Ensure this matches the dictionary key exactly

                    logging.info("Initial view set to: %s", self.initial_view)
            else:
                logging.error("session.json file not found.")
        except Exception as e:
            logging.error(f"An error occurred while initializing: {e}")

        self.switch_view(self.initial_view)

if __name__ == "__main__":
    import tkinter as tk
    root = tk.Tk()
    root.title("Main Application")
    controller = MainController(root)
    root.mainloop()
