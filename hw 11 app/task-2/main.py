import json
import sys

from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (
    QApplication,
    QButtonGroup,
    QCheckBox,
    QLabel,
    QMainWindow,
    QPushButton,
    QRadioButton,
    QVBoxLayout,
    QWidget,
)


class QuizApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.questions = self.load_questions()
        self.current_question = 0
        self.correct_answers = 0

        self.setWindowTitle("Тестовая система")
        self.setMinimumSize(400, 300)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        self.font = QFont()
        self.font.setPointSize(24)

        label_font = QFont()
        label_font.setPointSize(16)
        self.label = QLabel()
        self.label.setFont(label_font)
        self.label.setWordWrap(True)
        layout.addWidget(self.label)

        self.answers_group = QButtonGroup()
        self.answers_group.setExclusive(False)
        self.answers_layout = QVBoxLayout()
        layout.addLayout(self.answers_layout)

        self.submit_btn = QPushButton("Ответить")
        self.submit_btn.setFont(self.font)
        self.submit_btn.clicked.connect(self.check_answer)
        layout.addWidget(self.submit_btn)

        self.show_question()

    def load_questions(self):
        try:
            with open("questions.json", "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            print("Файл questions.json не найден")
            sys.exit()

    def show_question(self):
        if self.current_question >= len(self.questions):
            self.show_results()
            return

        question_data = self.questions[self.current_question]
        self.label.setText(question_data["question"])

        for i in reversed(range(self.answers_layout.count())):
            widget = self.answers_layout.itemAt(i).widget()
            if widget:
                widget.deleteLater()

        self.answer_widgets = []
        for i, answer in enumerate(question_data["answers"]):
            if question_data.get("multiple", False):
                checkbox = QCheckBox(answer)
                checkbox.setFont(self.font)
                self.answers_layout.addWidget(checkbox)
                self.answer_widgets.append(checkbox)
            else:
                radio = QRadioButton(answer)
                radio.setFont(self.font)
                self.answers_layout.addWidget(radio)
                self.answer_widgets.append(radio)

    def check_answer(self):
        question_data = self.questions[self.current_question]
        correct = question_data["correct"]
        user_answers = []

        for i, widget in enumerate(self.answer_widgets):
            if isinstance(widget, QCheckBox) and widget.isChecked():
                user_answers.append(i)
            elif isinstance(widget, QRadioButton) and widget.isChecked():
                user_answers.append(i)

        if sorted(user_answers) == sorted(correct):
            self.correct_answers += 1

        self.current_question += 1
        self.show_question()

    def show_results(self):
        total = len(self.questions)
        score = self.correct_answers
        percentage = (score / total) * 100

        result_text = f"Результаты:\nПравильных ответов: {score}/{total}\nПроцент: {percentage:.1f}%"
        self.label.setText(result_text)

        for i in reversed(range(self.answers_layout.count())):
            self.answers_layout.itemAt(i).widget().hide()
        self.submit_btn.hide()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QuizApp()
    window.show()
    sys.exit(app.exec())
