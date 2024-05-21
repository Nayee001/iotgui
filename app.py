import tkinter as tk
from controllers.main_controller import MainController
from common.constants import SCREEN_WIDTH, SCREEN_HEIGHT

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('IoT vFCL')
        self.geometry(f'{SCREEN_WIDTH}x{SCREEN_HEIGHT}')
        self.controller = MainController(self)

if __name__ == '__main__':
    app = MainApp()
    app.mainloop()
