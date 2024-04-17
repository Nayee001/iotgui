# mqtt_publisher.py
import paho.mqtt.client as paho
import json
import time
import logging
from mqtt_credentials import broker_address, client_name, port, user, password, topic
from models import encryption  # Import the encryption class

class MQTTPublisher:
    def __init__(self, encryption_key):
        self.encryption_key = encryption_key
        self.client = paho.Client(client_name)
        self.setup_mqtt()

    def on_publish(self, client, userdata, result):
        logging.info("Data Published to the Web Command Center")

    def setup_mqtt(self):
        self.client.username_pw_set(user, password=password)
        self.client.on_publish = self.on_publish
        self.client.connect(broker_address, port=port)

    def publish_data(self):
        data = {"encryption_key": self.encryption_key}
        payload = json.dumps(data)
        self.client.publish(topic, payload)
        logging.info("Published Encryption Key to the MQTT Topic.")

# Configure logging
logging.basicConfig(level=logging.INFO)

# Usage
project_directory = '/home/nayee001/Desktop/iotgui'
encryptor = encryption.DirectoryEncryptor(project_directory)
encryption_key = encryptor.encrypt_directory()

publisher = MQTTPublisher(encryption_key)

try:
    while True:
        publisher.publish_data()
        time.sleep(1)  # Adjust sleep time if necessary
except KeyboardInterrupt:
    logging.info("Exiting program")
finally:
    publisher.client.disconnect()
