# dashboard.py
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QMessageBox

class Dashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dashboard - Mental Health Tracker")
        self.setGeometry(100, 100, 400, 300)
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        self.welcome_label = QLabel("Welcome to the Dashboard!")
        layout.addWidget(self.welcome_label)

        self.mood_entry_button = QPushButton("Log Today's Mood")
        self.mood_entry_button.clicked.connect(self.log_mood)
        layout.addWidget(self.mood_entry_button)

        self.history_button = QPushButton("View Mood History")
        self.history_button.clicked.connect(self.view_history)
        layout.addWidget(self.history_button)

        self.setLayout(layout)

    def log_mood(self):
        QMessageBox.information(self, "Mood", "This will open the Mood Entry form!")

    def view_history(self):
        QMessageBox.information(self, "History", "This will show mood log history!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Dashboard()
    window.show()
    sys.exit(app.exec_())
