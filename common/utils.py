# File: utils.py
import logging

def get_device_status():
    status = {
        "status": "Unknown",
        "device_status": "Unknown",
        "health_status": "Unknown",
        "timestamps": "Unknown",
        "fault_status": "Unknown"
    }
    try:
        with open("session.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                if line.startswith("status="):
                    status["status"] = line.split("=")[1].strip()
                elif line.startswith("device_status="):
                    status["device_status"] = line.split("=")[1].strip()
                elif line.startswith("health_status="):
                    status["health_status"] = line.split("=")[1].strip()
                elif line.startswith("timestamps="):
                    status["timestamps"] = line.split("=")[1].strip()
                elif line.startswith("fault_status="):
                    status["fault_status"] = line.split("=")[1].strip()
    except FileNotFoundError:
        logging.error("Error: session.txt file not found.")
    except Exception as e:
        logging.error(f"An error occurred while reading the session file: {e}")
    
    return status
