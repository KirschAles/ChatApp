from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QTextEdit, QPushButton, QHBoxLayout, QLabel


class DataEntry(QWidget):
    def __init__(self, label):
        super(DataEntry, self).__init__()
        self.setLayout(QVBoxLayout)
        self.label = QLabel(label)
        self.field = QTextEdit()
        self.layout().addWidget(self.label)
        self.layout().addWidget(self.field)

    def text(self):
        # using cpp style text() to be style compliant with other pyqt5 widgets
        return self.field.toPlainText()

    def clear(self):
        self.field.setText('')


class Login(QWidget):
    def __init__(self):
        super(Login, self).__init__()
        self.setLayout(QVBoxLayout)
        self.title = QLabel('LOGIN')
        self.title.setFont(QFont('Arial', 30))
        self.add_widget(self.title)
        self.username = DataEntry('username')
        self.password = DataEntry('password')
        self.add_widget(self.username)
        self.add_widget(self.password)

        self.login = QPushButton('Login')
        self.register = QPushButton('Register')
        self.add_widget(self.login)
        self.add_widget(self.register)

    def add_widget(self, widget: QWidget) -> None:
        self.layout().addWidget(widget)

