import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QHBoxLayout
from cryptography.fernet import Fernet
import os
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


class PasswordManager(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password Manager")
        self.setGeometry(300, 300, 400, 200)

        # Create encryption key if it doesn't exist
        if not os.path.exists("secret.key"):
            self.generate_key()

        # Initialize UI
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()

        # Service name input
        self.service_label = QLabel("Enter Service Name:")
        self.service_input = QLineEdit()
        self.layout.addWidget(self.service_label)
        self.layout.addWidget(self.service_input)

        # Password input
        self.password_label = QLabel("Enter Password:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.layout.addWidget(self.password_label)
        self.layout.addWidget(self.password_input)

        # Encrypt Button
        self.encrypt_button = QPushButton("Store Password")
        self.encrypt_button.clicked.connect(self.store_password)
        self.layout.addWidget(self.encrypt_button)

        # Decrypt Button
        self.decrypt_button = QPushButton("Retrieve Password")
        self.decrypt_button.clicked.connect(self.retrieve_password)
        self.layout.addWidget(self.decrypt_button)

        # Result Display
        self.result_label = QLabel("Result will be shown here.")
        self.layout.addWidget(self.result_label)

        # Set layout
        self.setLayout(self.layout)

    def generate_key(self):
        """Generate a key for encryption and save it."""
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)

    def load_key(self):
        """Load the previously generated key."""
        return open("secret.key", "rb").read()

    def encrypt_password(self, password):
        """Encrypt the password."""
        key = self.load_key()
        f = Fernet(key)
        encrypted_password = f.encrypt(password.encode())
        return encrypted_password

    def decrypt_password(self, encrypted_password):
        """Decrypt the password."""
        key = self.load_key()
        f = Fernet(key)
        decrypted_password = f.decrypt(encrypted_password).decode()
        return decrypted_password

    def store_password(self):
        """Store the password securely."""
        service = self.service_input.text()
        password = self.password_input.text()

        if service and password:
            encrypted_password = self.encrypt_password(password)
            with open("passwords.txt", "a") as file:
                file.write(f"{service} : {encrypted_password.decode()}\n")
            self.result_label.setText(f"Password for {service} stored successfully!")
        else:
            self.result_label.setText("Please provide both service and password.")

    def retrieve_password(self):
        """Retrieve the password for a given service."""
        service = self.service_input.text()

        if service:
            found = False
            with open("passwords.txt", "r") as file:
                for line in file.readlines():
                    if service in line:
                        encrypted_password = line.split(":")[1].strip().encode()
                        decrypted_password = self.decrypt_password(encrypted_password)
                        self.result_label.setText(f"Password for {service} is: {decrypted_password}")
                        found = True
                        break

            if not found:
                self.result_label.setText("Service not found.")
        else:
            self.result_label.setText("Please provide a service name.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PasswordManager()
    window.show()
    sys.exit(app.exec_())
