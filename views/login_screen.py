import tkinter as tk
from tkinter import PhotoImage, messagebox
from common import constants
from models.api_connector import APIConnector
import json
import os

SESSION_FILE = "session.json"
FONT_NAME = "Arial"
PADDING_X = 150

class LoginScreen(tk.Frame):
    def __init__(self, controller):
        super().__init__(controller.root, width=constants.SCREEN_WIDTH, height=constants.SCREEN_HEIGHT, bg='white')
        self.controller = controller
        self.api_connector = APIConnector("http://172.20.120.101")

        # Load images
        self.logo_image = PhotoImage(file='iot.png')  # Replace with actual path
        self.left_arrow_image = PhotoImage(file='left.png')  # Replace with actual path

        self.setup_ui()

    def setup_ui(self):
        # Logo and Title
        tk.Label(self, image=self.logo_image, bg='white').pack(pady=(30, 10))
        tk.Label(self, text="Login to Device", font=(FONT_NAME, 24), bg='white').pack(pady=(5, 20))

        # Username Entry
        tk.Label(self, text="Username", font=(FONT_NAME, 16), bg='white').pack(anchor='w', padx=(PADDING_X, 0))
        self.username_entry = tk.Entry(self, font=(FONT_NAME, 16), width=25)
        self.username_entry.pack(pady=(5, 10), padx=PADDING_X)

        # Password Entry
        tk.Label(self, text="Password", font=(FONT_NAME, 16), bg='white').pack(anchor='w', padx=(PADDING_X, 0))
        self.password_entry = tk.Entry(self, font=(FONT_NAME, 16), width=25, show='*')
        self.password_entry.pack(pady=(5, 20), padx=PADDING_X)

        # Error Message
        self.error_label = tk.Label(self, text="", font=(FONT_NAME, 14), fg='red', bg='white')
        self.error_label.pack(pady=(5, 10), padx=PADDING_X)

        # Login Button
        login_button = tk.Button(self, text="Login", font=(FONT_NAME, 16), bg='#3C7DD9', fg='white', command=self.login)
        login_button.pack(pady=(10, 20), ipadx=10, ipady=5)

        # Back button
        back_button = tk.Button(self, image=self.left_arrow_image, command=lambda: self.controller.switch_view('config'), borderwidth=0, bg='white')
        back_button.image = self.left_arrow_image
        back_button.place(x=20, y=constants.SCREEN_HEIGHT - 50)

        self.pack_propagate(False)

    def login(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        self.error_label.config(text="")  # Clear any previous errors

        if not username or not password:
            self.error_label.config(text="Enter username and password.")
            return

        result = self.api_connector.login(username, password)

        if result and 'token' in result:
            self.store_session(result['token'])
            messagebox.showinfo("Login Successful", "You have logged in successfully!")
            self.after(1500, self.after_login)  # 1.5 sec delay before switching
        else:
            self.error_label.config(text="Invalid username or password.")

    def after_login(self):
        self.controller.switch_view('verifyDevice')

    def store_session(self, token):
        session_data = self.load_session_data()
        session_data.update({
            "session_active": True,
            "token": token
        })

        with open(SESSION_FILE, "w") as file:
            json.dump(session_data, file, indent=4)

    def load_session_data(self):
        if os.path.exists(SESSION_FILE):
            try:
                with open(SESSION_FILE, "r") as file:
                    return json.load(file)
            except json.JSONDecodeError:
                return {}
        return {}

if __name__ == '__main__':
    pass
