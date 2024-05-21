import tkinter as tk
from tkinter import PhotoImage
from common import constants

class ConfigScreen(tk.Frame):
    def __init__(self, controller):
        super().__init__(controller.root, width=constants.SCREEN_WIDTH, height=constants.SCREEN_HEIGHT, bg='white')
        self.controller = controller

        # Assuming 'iot.png' is the logo, make sure the path is correct relative to the main script file
        self.logo_image = PhotoImage(file='iot.png')
        self.logo_label = tk.Label(self, image=self.logo_image, bg='white')
        self.logo_label.pack(pady=(20, 0))  # Adjust padding as needed
        
        # Device Configuration Steps Label
        self.steps_label = tk.Label(self, text='Device Configuration Steps:', font=("Arial", 18), bg='white')
        self.steps_label.pack(pady=(10, 10))

        # Steps text
        steps_text = (
            "1. Please Use Another Computer to \nlogin into command center"
            "2. Log into Command Center. (http://172.20.120.101/)\n"
            "3. In Command center follow instructions \nto Confirm Device ID and Location.\n"
            "4. In Device management you`ll Get Device API Key.\n"
            "5. In next screen Use Command Center credentials to log into Device.\n"
            "6. Enter Device API Key and wait.\n"
            "7. Device ready!"
        )
        self.instructions_label = tk.Label(self, text=steps_text, font=("Arial", 12), bg='white', justify="left")
        self.instructions_label.pack(pady=(5, 20))

        # Left arrow button image
        self.left_button_image = PhotoImage(file='left.png')  # Replace with the correct path to the left arrow image
        self.left_button = tk.Button(self, image=self.left_button_image, command=lambda: controller.switch_view('welcome'), borderwidth=0, bg='white')
        self.left_button.place(relx=0, rely=1.0, x=10, y=-10, anchor='sw')

        # Right arrow button image
        self.right_button_image = PhotoImage(file='right.png')  # Replace with the correct path to the right arrow image
        self.right_button = tk.Button(self, image=self.right_button_image, command=lambda: controller.switch_view('login'), borderwidth=0, bg='white')
        self.right_button.place(relx=1.0, rely=1.0, x=-10, y=-10, anchor='se')


        self.left_button.image = self.left_button_image
        self.right_button.image = self.right_button_image
        

        self.pack_propagate(False)


if __name__ == '__main__':
    pass
