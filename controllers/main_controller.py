# Main Controller for routing 

from views.welcome_screen import WelcomeScreen
from views.config_screen import ConfigScreen
from views.login_screen import LoginScreen
from views.verify_device_screen import VerifyDeviceScreen
from views.device_getting_ready import DeviceGettingReadyScreen
from views.device_dashboard import DeviceDashboardScreen

class MainController:
    def __init__(self, root):
        self.root = root
        self.views = {
            'welcome': WelcomeScreen(self),
            'config': ConfigScreen(self),
            'Login': LoginScreen(self),
            'VerifyDevice': VerifyDeviceScreen(self),
            "DeviceGettingReadyScreen": DeviceGettingReadyScreen(self),
            "DeviceDashboardScreen": DeviceDashboardScreen(self)
        }
        self.current_view = None
        self.switch_view('welcome')

    def switch_view(self, view_name):
        if self.current_view is not None:
            self.current_view.pack_forget()
        self.current_view = self.views[view_name]
        self.current_view.pack()
