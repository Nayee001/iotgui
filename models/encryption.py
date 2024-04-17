# encryption_module.py
import os
from cryptography.fernet import Fernet

class DirectoryEncryptor:
    def __init__(self, directory):
        self.directory = directory
        self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)

    def encrypt_file(self, file_path):
        with open(file_path, 'rb') as file:
            file_data = file.read()
        encrypted_data = self.cipher.encrypt(file_data)
        with open(file_path, 'wb') as file:
            file.write(encrypted_data)

    def encrypt_directory(self):
        for root, dirs, files in os.walk(self.directory):
            for file in files:
                file_path = os.path.join(root, file)
                self.encrypt_file(file_path)
        return self.key.decode()  # Returns the key as a string for use elsewhere
