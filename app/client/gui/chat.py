from PyQt5.QtWidgets import QLineEdit, QPushButton, QLabel, QVBoxLayout
from app.common.response.ClientResponse import ClientResponse
import app.common.servercommands as cmd
import app.common.headers as headers


class ChatBox(QVBoxLayout):
    def __init__(self, chat_id):
        super().__init__()
        self.chat_id = chat_id
        self.chat = QLabel()
        self.chat.setWordWrap(True)
        self.chat_write = QLineEdit()
        self.chat_send = QPushButton("SEND")
        self.chat_send.clicked.connect(self.send_message)
        self.addWidget(self.chat)
        self.addWidget(self.chat_send)
        self.addWidget(self.chat_write)

    def send_message(self):
        original_text = self.chat.text()
        self.chat_write.setText('')
        response = ClientResponse([original_text])
        response.command = cmd.SEND_MESSAGE
        response.headers[headers.CHAT_ID] = self.chat_id
        
