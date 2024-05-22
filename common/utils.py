# File: utils.py
import logging
import json

def get_device_status():
    status = {
        "status": "Unknown",
        "device_status": "Unknown",
        "health_status": "Unknown",
        "timestamps": "Unknown",
        "fault_status": "Unknown"
    }
    try:
        with open("session.json", "r") as file:
            data = json.load(file)
            status["status"] = data.get("status", "Unknown")
            status["device_status"] = data.get("device_status", "Unknown")
            status["health_status"] = data.get("health_status", "Unknown")
            status["timestamps"] = data.get("timestamps", "Unknown")
            status["fault_status"] = data.get("fault_status", "Unknown")
    except FileNotFoundError:
        logging.error("Error: session.json file not found.")
    except json.JSONDecodeError:
        logging.error("Error: session.json file is not a valid JSON.")
    except Exception as e:
        logging.error(f"An error occurred while reading the session file: {e}")
    
    return status
