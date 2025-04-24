# signup.py
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox

class SignupForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Signup - Mental Health Tracker")
        self.setGeometry(100, 100, 300, 250)
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        self.label = QLabel("Create New Account")
        layout.addWidget(self.label)

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Username")
        layout.addWidget(self.username_input)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_input)

        self.confirm_password_input = QLineEdit()
        self.confirm_password_input.setPlaceholderText("Confirm Password")
        self.confirm_password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.confirm_password_input)

        self.register_button = QPushButton("Register")
        self.register_button.clicked.connect(self.register_user)
        layout.addWidget(self.register_button)

        self.setLayout(layout)

    def register_user(self):
        username = self.username_input.text()
        password = self.password_input.text()
        confirm = self.confirm_password_input.text()

        if not username or not password or not confirm:
            QMessageBox.warning(self, "Error", "All fields are required!")
        elif password != confirm:
            QMessageBox.warning(self, "Error", "Passwords do not match!")
        else:
            QMessageBox.information(self, "Success", "Registration simulated (DB code will come later).")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SignupForm()
    window.show()
    sys.exit(app.exec_())
