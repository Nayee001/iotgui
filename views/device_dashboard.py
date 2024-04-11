import tkinter as tk
from common import constants
from tkinter import PhotoImage

class DeviceDashboardScreen(tk.Frame):
    def __init__(self, controller):
        super().__init__(controller.root, width=constants.SCREEN_WIDTH, height=constants.SCREEN_HEIGHT, bg='white')
        self.controller = controller
        
        # Device Info Frame
        info_frame = tk.Frame(self, bg='white', borderwidth=1, relief='solid')
        info_frame.place(relx=0.75, rely=0.05, relwidth=0.2, relheight=0.3, anchor='n')
        
        # Device Title
        tk.Label(self, text="vFCL Device 001", font=("Arial", 24), bg='white').place(relx=0.5, rely=0.05, anchor='n')
        
        # Timestamp and Settings Icon
        tk.Label(self, text="5:30 PM March 15 2024 - |Hack 210, Gannon University",
                 font=("Arial", 10), bg='white').place(relx=0.5, rely=0.1, anchor='n')
        
        # Settings icon (assuming you have an image for settings)
        # settings_image = PhotoImage(file='path_to_your_settings_icon.png')  # Replace with the correct path
        # settings_button = tk.Button(info_frame, image=settings_image, bg='white', borderwidth=0)
        # settings_button.photo = settings_image  # Keep a reference
        # settings_button.pack(side='top', anchor='e', padx=10, pady=5)
        
        # Device Status Information
        status_text = "\n".join(["Device Status: Active",
                                 "Health Status: No Fault Occurs",
                                 "Timestamps: March 15 2024",
                                 "Fault Status: OFF"])
        tk.Label(info_frame, text=status_text, font=("Arial", 12), bg='white', justify='left').pack(side='top', anchor='w', padx=10, pady=5)
        
        # Graph Canvas
        graph_frame = tk.Frame(self, bg='white', borderwidth=1, relief='solid')
        graph_frame.place(relx=0.05, rely=0.2, relwidth=0.6, relheight=0.5)
        # Here you would actually create and pack a Canvas or a matplotlib FigureCanvasTkAgg if you're using matplotlib
        
        # Last Sync Status
        tk.Label(self, text="Last Sync: 03-15-2024: 4:00PM", font=("Arial", 10), bg='white').place(relx=0.05, rely=0.75, anchor='sw')

# The rest of your application setup code would go here.
