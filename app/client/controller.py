import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit, QPushButton, QLabel, QVBoxLayout, QWidget
from app.client.gui.conversations import Conversations
from app.client.gui.chat import ChatBox
from app.client.database.conversations import ConvDB


class MainWindow(QMainWindow):
    def __init__(self, conv_db):
        super(MainWindow, self).__init__()
        self.conv_db = conv_db
        self.conversations = Conversations(self.conv_db)
        self.start_conversations_window()

    def start_conversations_window(self):
        self.conversations = Conversations(self.conv_db)
        self.setCentralWidget(self.conversations)
        self.conversations.chat_buttons.buttonClicked.connect(self.start_chat_window)

    def start_chat_window(self, button):
        chat_id = self.conversations.chat_buttons.id(button)
        chat = ChatBox(self.conv_db[chat_id])
        self.setCentralWidget(chat)
        chat.back.clicked.connect(self.start_conversations_window)


app = QApplication(sys.argv)

conv_db = ConvDB()
window = MainWindow(conv_db)
window.show()
app.exec()