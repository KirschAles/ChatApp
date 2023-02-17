from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QPushButton, QLabel
from app.client.gui.widgets import DataEntry


class Login(QWidget):
    def __init__(self):
        super(Login, self).__init__()
        self.setLayout(QVBoxLayout())
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

