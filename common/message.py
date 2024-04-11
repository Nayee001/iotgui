import tkinter as tk
from tkinter import Toplevel, Label, PhotoImage

class MessagePopup:
    @staticmethod
    def show_error(master, message, image_path):
        error_popup = Toplevel(master)
        error_popup.title("Error")
        error_popup.geometry('200x100')
        error_popup.configure(bg='white')

        error_icon = PhotoImage(file=image_path)
        error_label = Label(error_popup, image=error_icon, bg='white')
        error_label.image = error_icon  # Keep a reference
        error_label.pack(pady=(10, 5))

        error_text = Label(error_popup, text=message, bg='white')
        error_text.pack()

        # Center the popup
        MessagePopup.center_popup(error_popup)

    @staticmethod
    def show_success(master, message):
        success_popup = Toplevel(master)
        success_popup.title("Success")
        success_popup.geometry('300x150')
        success_popup.configure(bg='white')

        success_label = Label(success_popup, text=message, bg='white')
        success_label.pack(pady=(20, 0))

        # Center the popup
        MessagePopup.center_popup(success_popup)

    @staticmethod
    def center_popup(popup):
        # Calculate position x, y to center the popup
        center_x = int(popup.winfo_screenwidth()/2 - 150)
        center_y = int(popup.winfo_screenheight()/2 - 75)
        popup.geometry(f'+{center_x}+{center_y}')
