# mood_entry.py
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QComboBox, QPushButton, QMessageBox

class MoodEntryForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mood Log - Mental Health Tracker")
        self.setGeometry(100, 100, 350, 250)
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        self.mood_label = QLabel("Select your mood:")
        layout.addWidget(self.mood_label)

        self.mood_combobox = QComboBox()
        self.mood_combobox.addItems(["Happy", "Sad", "Angry", "Anxious", "Excited"])
        layout.addWidget(self.mood_combobox)

        self.symptom_input = QLineEdit()
        self.symptom_input.setPlaceholderText("Describe any symptoms...")
        layout.addWidget(self.symptom_input)

        self.note_input = QLineEdit()
        self.note_input.setPlaceholderText("Additional notes...")
        layout.addWidget(self.note_input)

        self.submit_button = QPushButton("Submit Mood Log")
        self.submit_button.clicked.connect(self.submit_mood)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

    def submit_mood(self):
        mood = self.mood_combobox.currentText()
        symptoms = self.symptom_input.text()
        notes = self.note_input.text()

        QMessageBox.information(self, "Logged!", f"Mood: {mood}\nSymptoms: {symptoms}\nNotes: {notes}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MoodEntryForm()
    window.show()
    sys.exit(app.exec_())
