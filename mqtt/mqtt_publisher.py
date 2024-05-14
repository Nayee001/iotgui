# File: mqtt_publisher.py
import paho.mqtt.client as paho
import json
import time
import logging
from mqtt.mqtt_credentials import broker_address, client_name, port, user, password, topic


class MQTTPublisher:
    def __init__(self, encryption_key, api_key):
        self.encryption_key = encryption_key
        self.api_key = api_key
        self.client = paho.Client(client_name)
        self.setup_mqtt()

    def on_publish(self, client, userdata, result):
        logging.info("Data Published to the Web Command Center")

    def setup_mqtt(self):
        """Setup the MQTT client."""
        try:
            self.client.username_pw_set(user, password=password)
            self.client.on_publish = self.on_publish
            self.client.connect(broker_address, port=port)
        except Exception as e:
            logging.error(f"Failed to connect to MQTT broker: {e}")

    def publish_data(self):
        """Publish data using MQTT."""
        try:
            data = {"encryption_key": self.encryption_key, "api_key": self.api_key}
            payload = json.dumps(data)
            self.client.publish(topic, payload)
            logging.info("Published Encryption Key and API Key to the MQTT Topic.")
        except Exception as e:
            logging.error(f"Failed to publish data: {e}")
