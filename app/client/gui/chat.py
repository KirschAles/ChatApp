from PyQt5.QtWidgets import QLineEdit, QPushButton, QLabel, QVBoxLayout


class ChatBox(QVBoxLayout):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chat")
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
        self.chat.setText(original_text + '\n' + self.chat_write.text())
        self.chat_write.setText('')
