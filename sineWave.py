import json
import random
import time
from datetime import datetime
import paho.mqtt.client as mqtt

# MQTT Broker Configuration
server = "broker.hivemq.com"
port = 1883
username = ""
password = ""
client_id = "WebCommandCenter"
topic = "mqttdevice/6bfa9c/json_payload"

# Simulated device ID
getDevice = {'id': "6bfa9c"}

# MQTT Setup
client = mqtt.Client(client_id)
client.username_pw_set(username, password)
client.connect(server, port)

def generate_json_payload():
    # Simulated sensor values
    v1 = round(random.uniform(220, 230), 1)
    v2 = round(random.uniform(220, 230), 1)
    v3 = round(random.uniform(220, 230), 1)
    v_total = round(v1 + v2 + v3, 1)
    v_avg = round(v_total / 3, 1)

    c1 = round(random.uniform(0, 10), 2)
    c2 = round(random.uniform(0, 10), 2)
    c3 = round(random.uniform(0, 10), 2)
    c_total = round(c1 + c2 + c3, 2)

    event_data = {
        'LineVoltage1': v1,
        'LineVoltage2': v2,
        'LineVoltage3': v3,
        'LineVoltageTotal': v_total,
        'LineVoltageAverage': v_avg,
        'LineCurrentCT1': c1,
        'LineCurrentCT2': c2,
        'LineCurrentCT3': c3,
        'LineCurrentTotal': c_total
    }

    deviceData = {
        'topic': topic,
        'health_status': 'HEALTHY',
        'timestamps': datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),
        'event_data': event_data
    }

    data = {
        'device_api': getDevice['id'],
        'fault_status': 'ON',
        'topic': deviceData['topic'],
        'health_status': deviceData['health_status'],
        'timestamp': deviceData['timestamps'],
        'event_data': json.dumps(deviceData['event_data'])
    }

    return json.dumps(data)

# Loop to publish every second
while True:
    payload = generate_json_payload()
    client.publish(topic, payload)
    print(f"[MQTT Published] → {topic}: {payload}")
    client.loop()
    time.sleep(1)
