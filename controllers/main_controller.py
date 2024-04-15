from views.welcome_screen import WelcomeScreen
from views.config_screen import ConfigScreen
from views.login_screen import LoginScreen
from views.verify_device_screen import VerifyDeviceScreen
from views.device_getting_ready import DeviceGettingReadyScreen
from views.device_dashboard import DeviceDashboardScreen
import re  # Import regular expressions

class MainController:
    def __init__(self, root):
        self.root = root
        self.views = {
            'welcome': WelcomeScreen(self),
            'config': ConfigScreen(self),
            'Login': LoginScreen(self),  # Make sure the key is lowercase
            'VerifyDevice': VerifyDeviceScreen(self),  # Make sure the key is correctly cased
            'deviceGettingReady': DeviceGettingReadyScreen(self),  # Make sure the key is correctly cased
            'deviceDashboard': DeviceDashboardScreen(self)  # Make sure the key is correctly cased
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
            print("Switched to view:", view_name)
        except KeyError:
            print(f"View '{view_name}' does not exist. Please check the dictionary keys.")
        except Exception as e:
            print("An error occurred while switching views:", e)

    def check_session_and_initialize(self):
        try:
            with open('session.txt', 'r') as file:
                data = file.read()
                print("Session data read from file:", data)
                session_active = 'session_active=True' in data
                token_available = re.search(r'\d+\|[\w+]+', data) is not None  

            if session_active and token_available:
                self.initial_view = 'VerifyDevice'  # Ensure this matches the dictionary key exactly
            elif session_active:
                self.initial_view = 'Login'  # Ensure this matches the dictionary key exactly
            else:
                self.initial_view = 'welcome'  # Ensure this matches the dictionary key exactly

            print("Initial view set to:", self.initial_view)
        except FileNotFoundError:
            print("Error: session.txt file not found.")
        except Exception as e:
            print("An error occurred while initializing:", e)

        self.switch_view(self.initial_view)
