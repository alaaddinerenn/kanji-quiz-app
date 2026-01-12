from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from .meaning_quiz import MeaningQuiz
from .reading_quiz import ReadingQuiz
from .quiz_settings import QuizSettings
from utils.data_loader import get_kanji_meanings, get_kanji_readings, load_kanji_data

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kanji Quiz Application")
        self.setGeometry(400, 200, 600, 500)
        self.meaning_quiz_window = None
        self.reading_quiz_window = None
        
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        layout.setSpacing(10)                  # vertical space between widgets
        layout.setContentsMargins(16, 12, 16, 12)  # left, top, right, bottom margins

        # Big title label (English + Japanese)
        title = QLabel("Kanji Quiz — 漢字クイズ")
        title.setAlignment(Qt.AlignCenter)
        title_font = QFont("Helvetica", 20, QFont.Bold)
        title.setFont(title_font)

        layout.addWidget(title)

        meaning_quiz_button = QPushButton("Meaning Quiz")
        meaning_quiz_button.setMinimumHeight(80)
        bfont = QFont("Helvetica", 16)
        # tighten letter spacing a bit if needed
        try:
            bfont.setLetterSpacing(QFont.AbsoluteSpacing, -0.5)
        except Exception:
            pass
        meaning_quiz_button.setFont(bfont)
        # reduce internal padding so text doesn't look too far apart
        meaning_quiz_button.setStyleSheet("padding: 10px 14px;")

        meaning_quiz_button.clicked.connect(self.start_meaning_quiz)

        reading_quiz_button = QPushButton("Reading Quiz")
        reading_quiz_button.setMinimumHeight(80)
        reading_quiz_button.setFont(bfont)
        reading_quiz_button.setStyleSheet("padding: 10px 14px;")

        reading_quiz_button.clicked.connect(self.start_reading_quiz)

        layout.addWidget(meaning_quiz_button)
        layout.addWidget(reading_quiz_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def start_meaning_quiz(self):
        settings = QuizSettings(self)
        settings.move(
            self.x() + (self.width() - settings.width()) // 2,
            self.y() + (self.height() - settings.height()) // 2
        )
        if settings.exec_():
            question_count = settings.get_question_count()
            kanji_data = load_kanji_data()
            self.meaning_quiz_window = MeaningQuiz(get_kanji_meanings(kanji_data), question_count)
            self.meaning_quiz_window.finished_signal = self.show_main_window
            self.meaning_quiz_window.show()
            self.hide()

    def start_reading_quiz(self):
        settings = QuizSettings(self)
        settings.move(
            self.x() + (self.width() - settings.width()) // 2,
            self.y() + (self.height() - settings.height()) // 2
        )
        if settings.exec_():
            question_count = settings.get_question_count()
            kanji_data = load_kanji_data()
            self.reading_quiz_window = ReadingQuiz(get_kanji_readings(kanji_data), question_count)
            self.reading_quiz_window.finished_signal = self.show_main_window
            self.reading_quiz_window.show()
            self.hide()

    def show_main_window(self):
        self.show()