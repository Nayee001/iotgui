# api_connector.py
import requests


class APIConnector:
    def __init__(self, base_url):
        self.base_url = base_url

    def login(self, username, password):
        """Attempt to login with the provided username and password."""
        url = f"{self.base_url}/api/login"
        payload = {"email": username, "password": password}
        print(payload)
        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()  # Raises an exception for HTTP errors
            return response.json()  # Assuming JSON response
        except requests.exceptions.RequestException as e:
            print(e)  # For debugging purposes, adjust error handling as needed
            return None

    def verify_device(self, mac_address, api_key, token):
        """Verify device using the provided MAC address and API key."""
        url = f"{self.base_url}/api/verifyDevice"
        headers = {"Authorization": f"Bearer {token}"}
        payload = {"mac_address": mac_address, "apikey": api_key}
        try:
            response = requests.post(url, json=payload, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(e)
            return None
