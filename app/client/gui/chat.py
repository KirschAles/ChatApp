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
        self.chat_window = QLabel()
        self.load_chat()
        self.layout().addWidget(self.chat_window)
        self.send_button = QPushButton('Send')
        self.send_button.clicked.connect(self.send_message)
        self.layout().addWidget(self.send_button)
        self.message = QLineEdit()
        self.layout().addWidget(self.message)

    def load_chat(self):
        for message in self.chat.messages:
            self.chat_window.setText(self.chat_window.text() + str(message) + '\n')

    def send_message(self):
        text = self.message.text()
        self.chat.add_message(text, self.username)
        self.chat_window.setText(self.chat_window.text() + str(self.chat.last_message) + '\n')



