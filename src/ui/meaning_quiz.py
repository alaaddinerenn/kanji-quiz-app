from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QGridLayout, QMessageBox, QHBoxLayout
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont
import random

class MeaningQuiz(QWidget):
    def __init__(self, kanji_data, question_count=10):
        super().__init__()
        self.kanji_data = kanji_data
        self.question_count = question_count
        self.current_question = 0
        self.correct_answers = 0
        self.wrong_answers = 0
        self.asked_kanji = set()
        self.current_kanji = None
        self.init_ui()
        self.load_question()

    def init_ui(self):
        self.setWindowTitle('Kanji Meaning Quiz')
        self.setGeometry(400, 200, 600, 500)

        # Score label (top right)
        self.score_label = QLabel(self)
        self.score_label.setAlignment(Qt.AlignRight)
        score_font = QFont('Helvetica', 14, QFont.Bold)
        self.score_label.setFont(score_font)
        self.update_score()

        self.kanji_label = QLabel(self)
        self.kanji_label.setAlignment(Qt.AlignCenter)
        font = QFont()
        font.setPointSize(72)
        self.kanji_label.setFont(font)

        self.option_buttons = [QPushButton(self) for _ in range(4)]
        bfont = QFont("Helvetica", 16)
        try:
            bfont.setLetterSpacing(QFont.AbsoluteSpacing, -0.5)
        except Exception:
            pass
        for btn in self.option_buttons:
            btn.setMinimumHeight(100)
            btn.setFont(bfont)
            btn.setStyleSheet("border: 2px solid #444; border-radius: 8px; text-align: center; padding: 8px 12px; color: white; background: none;")
        for i, btn in enumerate(self.option_buttons):
            btn.clicked.connect(lambda _, idx=i: self.option_clicked(idx))

        layout = QVBoxLayout()
        layout.setSpacing(8)
        layout.setContentsMargins(12, 10, 12, 10)
        
        layout.addWidget(self.score_label)
        layout.addWidget(self.kanji_label, stretch=2)

        grid = QGridLayout()
        grid.setSpacing(8)
        grid.addWidget(self.option_buttons[0], 0, 0)
        grid.addWidget(self.option_buttons[1], 0, 1)
        grid.addWidget(self.option_buttons[2], 1, 0)
        grid.addWidget(self.option_buttons[3], 1, 1)

        layout.addLayout(grid, stretch=1)
        self.setLayout(layout)

    def update_score(self):
        self.score_label.setText(f'✓ {self.correct_answers}  ✗ {self.wrong_answers}  ({self.current_question}/{self.question_count})')

    def load_question(self):
        if self.current_question >= self.question_count:
            self.show_results()
            return

        for btn in self.option_buttons:
            btn.setEnabled(True)
            btn.setStyleSheet("border: 2px solid #444; border-radius: 8px; text-align: center; padding: 8px 12px; color: white; background: none;")

        if not self.kanji_data:
            QMessageBox.warning(self, 'Error', 'No kanji data available!')
            return

        # Get available kanji (not yet asked)
        available_kanji = [k for k in self.kanji_data.keys() if k not in self.asked_kanji]
        if not available_kanji:
            self.show_results()
            return

        self.current_kanji = random.choice(available_kanji)
        self.asked_kanji.add(self.current_kanji)
        self.kanji_label.setText(self.current_kanji)

        def make_meaning_text(meanings):
            if isinstance(meanings, str):
                return meanings
            if not isinstance(meanings, list):
                try:
                    return str(meanings)
                except Exception:
                    return ""
            picked = meanings[:3]
            return " / ".join(picked)

        correct_text = make_meaning_text(self.kanji_data[self.current_kanji])

        other_kanji = [k for k in self.kanji_data.keys() if k != self.current_kanji]
        if len(other_kanji) < 3:
            QMessageBox.warning(self, 'Error', 'Not enough kanji data!')
            return
        wrong_kanji = random.sample(other_kanji, 3)
        wrong_texts = [make_meaning_text(self.kanji_data[k]) for k in wrong_kanji]

        options = [correct_text] + wrong_texts
        random.shuffle(options)

        for btn, option in zip(self.option_buttons, options):
            btn.setText(option)
            try:
                btn.setChecked(False)
            except Exception:
                pass

    def option_clicked(self, index):
        for btn in self.option_buttons:
            btn.setEnabled(False)

        selected_button = self.option_buttons[index]
        correct_meaning = (self.kanji_data[self.current_kanji] if isinstance(self.kanji_data[self.current_kanji], str)
                           else " / ".join(self.kanji_data[self.current_kanji][:3]) )

        if selected_button.text() == correct_meaning:
            self.correct_answers += 1
            selected_button.setStyleSheet("border: 2px solid #28A745; border-radius: 8px; text-align: center; padding: 8px 12px; color: white; background-color: #28A745;")
            self.current_question += 1
            self.update_score()
            QTimer.singleShot(1500, self.load_question)
        else:
            self.wrong_answers += 1
            selected_button.setStyleSheet("border: 2px solid #DC3545; border-radius: 8px; text-align: center; padding: 8px 12px; color: white; background-color: #DC3545;")
            self.current_question += 1
            self.update_score()
            QTimer.singleShot(1000, lambda: self.show_correct_answer(correct_meaning))

    def show_correct_answer(self, correct_meaning):
        for btn in self.option_buttons:
            if btn.text() == correct_meaning:
                btn.setStyleSheet("border: 2px solid #28A745; border-radius: 8px; text-align: center; padding: 8px 12px; color: white; background-color: #28A745;")
                break
        QTimer.singleShot(2000, self.load_question)

    def show_results(self):
        percentage = (self.correct_answers / self.question_count * 100) if self.question_count > 0 else 0
        msg = QMessageBox(self)
        msg.setWindowTitle('Quiz Results')
        msg.setText(f'Quiz Completed!\n\nCorrect Answers: {self.correct_answers}\nWrong Answers: {self.wrong_answers}\nPercentage: {percentage:.2f}%')
        msg.setStandardButtons(QMessageBox.Ok)
        msg.buttonClicked.connect(self.close_quiz)
        msg.exec_()

    def close_quiz(self):
        self.close()
        import sys
        sys.exit()