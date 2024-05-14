import tkinter as tk
from tkinter import PhotoImage
from common import constants

class DeviceGettingReadyScreen(tk.Frame):
    def __init__(self, controller):
        super().__init__(controller.root, width=constants.SCREEN_WIDTH, height=constants.SCREEN_HEIGHT, bg='white')
        self.controller = controller

        # Message Label
        message_label = tk.Label(self, text="Please Check Command Center or Emails\n Accept your device from your command center\nPlease do not power off the device during this process.",
                                 font=("Arial", 14), bg='white', justify=tk.CENTER, padx=20)
        message_label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        # Schedule the dashboard button to appear after a few seconds
        self.after(5000, self.show_dashboard_button)  # 5000 milliseconds = 5 seconds

    def show_dashboard_button(self):
        # Button to proceed to the dashboard, appears after delay
        dashboard_button = tk.Button(self, text="Go to Dashboard", font=("Arial", 14), command=self.proceed_to_dashboard)
        dashboard_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

    def proceed_to_dashboard(self):
        # Transition to the device dashboard screen
        self.controller.switch_view('DeviceDashboardScreen')
