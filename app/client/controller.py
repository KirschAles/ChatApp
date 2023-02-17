import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit, QPushButton, QLabel, QVBoxLayout, QWidget
from app.client.gui.conversations import Conversations
from app.client.gui.chat import ChatBox
from app.client.database.conversations import ConvDB
from app.client.gui.login import Login


class MainWindow(QMainWindow):
    def __init__(self, conv_db: ConvDB):
        super(MainWindow, self).__init__()
        self.conv_db = conv_db
        self.conversations = Conversations(self.conv_db)
        self.login = None
        self.start_login_window()

    def start_conversations_window(self):
        self.conversations = Conversations(self.conv_db)
        self.setCentralWidget(self.conversations)
        self.conversations.chat_buttons.buttonClicked.connect(self.start_chat_window)

    def start_chat_window(self, button):
        chat_id = self.conversations.chat_buttons.id(button)
        chat = ChatBox(self.conv_db[chat_id], self.conv_db.username)
        self.setCentralWidget(chat)
        chat.back.clicked.connect(self.start_conversations_window)

    def login_user(self):
        username = self.login.username.text()
        password = self.login.password.text()
        self.conv_db = ConvDB(username, password)
        self.start_conversations_window()

    def start_login_window(self):
        self.login = Login()
        self.setCentralWidget(self.login)
        self.login.login.clicked.connect(self.login_user)


app = QApplication(sys.argv)

conv_db = ConvDB('username')
window = MainWindow(conv_db)
window.show()
app.exec()