from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QPushButton, QLabel
from app.client.gui.widgets import DataEntry


class Login(QWidget):
    def __init__(self):
        super(Login, self).__init__()
        self.setLayout(QVBoxLayout())
        self._title = QLabel('LOGIN')
        self._title.setFont(QFont('Arial', 30))
        self._add_widget(self._title)
        self._username = DataEntry('username')
        self._password = DataEntry('password')
        self._add_widget(self._username)
        self._add_widget(self._password)

        self.login = QPushButton('Login')
        self.register = QPushButton('Register')
        self._add_widget(self.login)
        self._add_widget(self.register)

    def _add_widget(self, widget: QWidget) -> None:
        self.layout().addWidget(widget)

    @property
    def username(self) -> str:
        return self._username.text()

    @property
    def password(self) -> str:
        return self._password.text()