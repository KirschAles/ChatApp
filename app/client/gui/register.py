from app.client.gui.widgets import DataEntry
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton


class Register(QWidget):
    def __init__(self):
        super(Register, self).__init__()
        self._layout = QVBoxLayout()
        self.setLayout(self._layout)

        self._username = DataEntry('username')
        self._password_first = DataEntry('password')
        self._password_second = DataEntry('password')
        self._layout.addWidget(self._username)
        self._layout.addWidget(self._password_first)
        self._layout.addWidget(self._password_second)

        buttons = QHBoxLayout()
        self._back = QPushButton('Back')
        self._register = QPushButton('Register')
        buttons.addWidget(self._back)
        buttons.addWidget(self._register)
        self._buttons = QWidget()
        self._buttons.setLayout(buttons)
        self._layout.addWidget(self._buttons)

    def password(self) -> str:
        return self._password_first.text()

    def username(self) -> str:
        return self._username.text()

    def clear_password(self) -> None:
        self._password_first.clear()
        self._password_second.clear()

    def are_passwords_equal(self) -> bool:
        return self._password_first.text() == self._password_second.text()

    @property
    def back(self):
        return self._back

    @property
    def register(self):
        return self._register
