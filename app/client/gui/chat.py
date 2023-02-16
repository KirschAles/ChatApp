from PyQt5.QtWidgets import QLineEdit, QPushButton, QLabel, QVBoxLayout, QWidget
from app.client.database.chat import ChatDB


class ChatBox(QWidget):
    def __init__(self, chat: ChatDB, user: str):
        super().__init__()
        self.username = user
        self.chat = chat
        self.back = QPushButton('Back')
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.back)



