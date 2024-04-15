import tkinter as tk
from tkinter import PhotoImage
from common import constants, message
from models.api_connector import APIConnector
import time
import threading

class LoginScreen(tk.Frame):
    def __init__(self, controller):
        super().__init__(controller.root, width=constants.SCREEN_WIDTH, height=constants.SCREEN_HEIGHT, bg='white')
        self.controller = controller
        self.api_connector = APIConnector("http://172.20.120.101")

        # Logo and Title
        self.logo_image = PhotoImage(file='iot.png')  # Replace with the correct path to the logo
        logo_label = tk.Label(self, image=self.logo_image, bg='white')
        logo_label.pack(pady=(30, 10))
        title_label = tk.Label(self, text="Login to Device", font=("Arial", 24), bg='white')
        title_label.pack(pady=(5, 20))

        # Username Entry
        tk.Label(self, text="Username", font=("Arial", 16), bg='white').pack(anchor='w', padx=(150, 0))
        self.username_entry = tk.Entry(self, font=("Arial", 16), width=20)
        self.username_entry.pack(pady=(5, 10), padx=150)

        # Password Entry
        tk.Label(self, text="Password", font=("Arial", 16), bg='white').pack(anchor='w', padx=(150, 0))
        self.password_entry = tk.Entry(self, font=("Arial", 16), width=20, show='*')
        self.password_entry.pack(pady=(5, 20), padx=150)

        # Error Message Label (Initially hidden)
        self.error_label = tk.Label(self, text="", font=("Arial", 16), fg='red', bg='white')
        self.error_label.pack(pady=(5, 10), padx=150)

        # Login Button
        login_button = tk.Button(self, text="Login", font=("Arial", 16), bg='#3C7DD9', fg='white', command=self.login)
        login_button.pack(pady=(10, 20), ipadx=10, ipady=5)

        # Left arrow button image for going back
        left_arrow_image = PhotoImage(file='left.png')  # Replace with the correct path
        left_button = tk.Button(self, image=left_arrow_image, command=lambda: controller.switch_view('config'), borderwidth=0, bg='white')
        left_button.image = left_arrow_image  # Keep a reference so it's not garbage collected
        left_button.place(x=20, y=constants.SCREEN_HEIGHT-30)

        self.pack_propagate(False)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        result = self.api_connector.login(username, password)
        
        if result and 'token' in result:
            token = result['token']
            self.store_session(token)
            tk.messagebox.showinfo("Login Successful", "You have logged in successfully!")

            self.after(3000, self.after_login)  # Use Tkinter's after for safe delay
        elif username == "" and password == "":
            self.error_label.config(text="Enter Username Password.")
        else:
            # Show error message
            self.error_label.config(text="Invalid username or password.")

    def after_login(self):
        # This method now is expected to be called from the main thread
        # Store session locally
        # self.store_session()
        # Switch to the next screen
        self.controller.switch_view('VerifyDevice')  # Proceed to verify device screen


    def store_session(self, token):
        # Storing the bearer token in a file
        print(token)
        with open("session.txt", "w") as session_file:
            session_file.write(f"session_active=True\ntoken={token}")

if __name__ == '__main__':
    pass
