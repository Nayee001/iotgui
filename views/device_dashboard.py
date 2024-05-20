import tkinter as tk
from common import constants
from common.utils import get_device_status
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.animation as animation
import numpy as np
import paho.mqtt.client as mqtt
from mqtt.mqtt_credentials import broker_address, client_name, port, user, password, topic

class DeviceDashboardScreen(tk.Frame):
    def __init__(self, controller):
        super().__init__(controller.root, width=constants.SCREEN_WIDTH, height=constants.SCREEN_HEIGHT, bg='white')
        self.controller = controller

        # Title and subtitle
        tk.Label(self, text="vFCL Device 001", font=("Arial", 20), bg='white').place(relx=0.05, rely=0.05, anchor='w')
        tk.Label(self, text="5:30 PM March 15 2024 - I Hack 210, Gannon University", font=("Arial", 10), bg='white').place(relx=0.05, rely=0.1, anchor='w')
        
        # Settings Icon
        settings_icon = tk.Label(self, text="⚙️", font=("Arial", 20), bg='white')
        settings_icon.place(relx=0.95, rely=0.05, anchor='e')

        # Graph Frame
        graph_frame = tk.Frame(self, bg='white', borderwidth=1, relief='solid')
        graph_frame.place(relx=0.05, rely=0.2, relwidth=0.6, relheight=0.5)
        self.setup_graph(graph_frame)
        tk.Label(self, text="Last Sync: 03-15-2024: 4:00PM", font=("Arial", 10), bg='white').place(relx=0.05, rely=0.75, anchor='sw')

        # Info Frame
        info_frame = tk.Frame(self, bg='white', borderwidth=1, relief='solid')
        info_frame.place(relx=0.7, rely=0.2, relwidth=0.25, relheight=0.5, anchor='n')
        
        # Get the device status
        status = get_device_status()
        
        status_text = "\n".join([
            f"Device Status: {status['status']}",
            f"Health Status: {status['health_status']}",
            f"Timestamps: {status['timestamps']}",
            f"Fault Status: {status['fault_status']}"
        ])

        status_color = 'green' if status['status'].lower() == 'approve' else 'red'
        tk.Label(info_frame, text=status_text, font=("Arial", 12), bg='white', fg=status_color, justify='left').pack(side='top', anchor='w', padx=10, pady=5)
        
        # If status is approved, trigger MQTT subscription
        if status['status'].lower() == 'approve':
            self.setup_mqtt()

    def setup_graph(self, frame):
        # Create a figure for the line chart
        self.fig = Figure(figsize=(5, 4), dpi=100)
        self.ax = self.fig.add_subplot(111)
        
        # Initial data
        self.x_data = np.linspace(0, 2*np.pi, 100)
        self.y_data = np.sin(self.x_data)
        self.line, = self.ax.plot(self.x_data, self.y_data, marker='o')
        
        # Customize the plot
        self.ax.set_xlabel("Timestamps")
        self.ax.set_ylabel("Volts")
        self.ax.grid(True)
        
        # Embedding the Matplotlib figure into Tkinter canvas
        self.canvas = FigureCanvasTkAgg(self.fig, master=frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH)
        
        # Animation for live updating
        self.ani = animation.FuncAnimation(self.fig, self.update_chart, interval=1000)

    def update_chart(self, i):
        # Update y_data with new values (this is where you fetch new data)
        self.y_data = np.sin(self.x_data + i/10.0)
        self.line.set_ydata(self.y_data)
        self.ax.relim()
        self.ax.autoscale_view()
        self.canvas.draw()

    def setup_mqtt(self):
        self.mqtt_client = mqtt.Client(client_name)
        self.mqtt_client.username_pw_set(user, password)
        self.mqtt_client.on_connect = self.on_connect
        self.mqtt_client.on_message = self.on_message
        self.mqtt_client.connect(broker_address, port, 60)
        self.mqtt_client.loop_start()

    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code " + str(rc))
        # Subscribe to a topic
        client.subscribe(topic)

    def on_message(self, client, userdata, msg):
        print(msg.topic + " " + str(msg.payload))
        # Process the received data and update the chart
        try:
            data = float(msg.payload.decode())
            self.update_live_data(data)
        except ValueError:
            print("Error: Could not convert MQTT message to float")

    def update_live_data(self, new_data):
        # Shift the x_data and append the new data point
        self.x_data = np.roll(self.x_data, -1)
        self.x_data[-1] = self.x_data[-1] + np.pi / 50
        # Append new data to y_data
        self.y_data = np.roll(self.y_data, -1)
        self.y_data[-1] = new_data
        self.line.set_ydata(self.y_data)
        self.ax.relim()
        self.ax.autoscale_view()
        self.canvas.draw()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Device Dashboard")
    controller = type('Controller', (object,), {'root': root})
    app = DeviceDashboardScreen(controller)
    app.pack(fill='both', expand=True)
    root.mainloop()
