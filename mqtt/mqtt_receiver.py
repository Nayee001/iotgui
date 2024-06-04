import paho.mqtt.client as mqtt
import json
import os
import logging
from mqtt.mqtt_credentials import broker_address, client_name, port, user, password, topic

# MQTT credentials and topic information
BROKER_ADDRESS = broker_address
CLIENT_NAME = client_name
PORT = port  # Default MQTT port
USER = user
PASSWORD = password
TOPIC = topic

# Path to the session file
SESSION_FILE_PATH = "session.json"

# Function to handle incoming MQTT messages
def on_message(client, userdata, msg):
    logging.info(f"Received message: {msg.payload.decode()} on topic {msg.topic}")
    message = msg.payload.decode().lower()
    print(message)
    if message == "reset":
        reset_session_data()

# Function to reset the session data
def reset_session_data():
    try:
        if os.path.exists(SESSION_FILE_PATH):
            with open(SESSION_FILE_PATH, "w") as file:
                json.dump({}, file)
            logging.info("Session data reset successfully.")
        else:
            logging.warning("Session file not found. Nothing to reset.")
    except Exception as e:
        logging.error(f"Error resetting session data: {e}")

# Function to setup and run the MQTT client
def mqtt_receiver():
    client = mqtt.Client(CLIENT_NAME)
    client.username_pw_set(USER, PASSWORD)
    client.on_connect = lambda client, userdata, flags, rc: client.subscribe(TOPIC)
    client.on_message = on_message
    client.connect(BROKER_ADDRESS, PORT, 60)
    
    logging.info("MQTT receiver started")
    client.loop_forever()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    mqtt_receiver()
