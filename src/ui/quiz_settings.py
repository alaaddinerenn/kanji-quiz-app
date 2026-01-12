from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QSpinBox, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class QuizSettings(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.question_count = 10
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Quiz Settings')
        self.setGeometry(500, 300, 300, 150)

        layout = QVBoxLayout()
        layout.setSpacing(15)
        layout.setContentsMargins(20, 20, 20, 20)

        label = QLabel('How many questions?')
        label.setAlignment(Qt.AlignCenter)
        font = QFont('Helvetica', 12)
        label.setFont(font)

        self.spin_box = QSpinBox()
        self.spin_box.setMinimum(1)
        self.spin_box.setMaximum(50)
        self.spin_box.setValue(50)
        self.spin_box.setFont(QFont('Helvetica', 14))
        self.spin_box.setMinimumHeight(40)

        start_button = QPushButton('Start')
        start_button.setMinimumHeight(50)
        start_button.setFont(QFont('Helvetica', 14))
        start_button.clicked.connect(self.accept)

        layout.addWidget(label)
        layout.addWidget(self.spin_box)
        layout.addWidget(start_button)

        self.setLayout(layout)

    def get_question_count(self):
        return self.spin_box.value()