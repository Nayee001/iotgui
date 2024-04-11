import tkinter as tk
from tkinter import PhotoImage
from common import constants

class WelcomeScreen(tk.Frame):
    def __init__(self, controller):
        super().__init__(controller.root, width=constants.SCREEN_WIDTH, height=constants.SCREEN_HEIGHT, bg='white')
        self.controller = controller
        
        # Assuming 'iot.png' is the logo, make sure the path is correct relative to the main script file
        self.logo_image = PhotoImage(file='iot.png')
        self.logo_label = tk.Label(self, image=self.logo_image, bg='white')
        self.logo_label.pack(pady=(120, 0))  # Adjust padding as needed
        
        # Welcome text
        self.welcome_label = tk.Label(self, text="Welcome to vFCL", font=("Arial", 24), bg='white')
        self.welcome_label.pack(pady=(10, 0))  # Adjust padding as needed

        # Right arrow button image
        self.right_button_image = PhotoImage(file='right.png') 
        self.right_button = tk.Button(self, image=self.right_button_image, command=lambda: controller.switch_view('config'), borderwidth=0, bg='white')
        self.right_button.place(relx=1.0, rely=1.0, x=-10, y=-10, anchor='se')
        self.logo_label.image = self.logo_image
        self.right_button.image = self.right_button_image
        

        self.pack_propagate(False)


if __name__ == '__main__':
    pass
