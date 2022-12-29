import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit, QPushButton, QLabel, QVBoxLayout, QWidget


class ChatWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chat")
        self.chat = QLabel()
        self.chat.setWordWrap(True)
        self.chat_write = QLineEdit()
        self.chat_send = QPushButton("SEND")
        self.chat_send.clicked.connect(self.send_message)
        layout = QVBoxLayout()
        layout.addWidget(self.chat)
        layout.addWidget(self.chat_send)
        layout.addWidget(self.chat_write)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def send_message(self):
        original_text = self.chat.text()
        self.chat.setText(original_text + '\n' + self.chat_write.text())
        self.chat_write.setText('')


app = QApplication(sys.argv)


window = ChatWindow()
window.show()
app.exec()