# File: encryption.py
import os
from cryptography.fernet import Fernet

class DirectoryEncryptor:
    def __init__(self, directory):
        self.directory = directory
        self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)

    def encrypt_file(self, file_path):
        """Encrypt a file using the provided cipher."""
        try:
            with open(file_path, 'rb') as file:
                file_data = file.read()
            encrypted_data = self.cipher.encrypt(file_data)
        except Exception as e:
            print(f"Failed to encrypt {file_path}: {e}")

    def encrypt_directory(self):
        """Encrypt all files in the directory recursively."""
        for root, dirs, files in os.walk(self.directory):
            for file in files:
                file_path = os.path.join(root, file)
                self.encrypt_file(file_path)
        return self.key.decode()  # Returns the encryption key as a string

# Example usage (this part can be removed or commented out when integrating with other scripts)
if __name__ == '__main__':
    project_directory = '/home/nayee001/Desktop/iotgui'
    encryptor = DirectoryEncryptor(project_directory)
    encryption_key = encryptor.encrypt_directory()
    print("Encryption Key:", encryption_key)
