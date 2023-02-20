import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit, QPushButton, QLabel, QVBoxLayout, QWidget
from app.client.gui.conversations import Conversations
from app.client.gui.chat import ChatBox
from app.client.database.conversations import ConvDB
from app.client.gui.login import Login
from app.client.gui.register import Register
from app.common.request.requestformat import RequestFormat
import app.common.servercommands as cmd
import app.common.headers as headers
from app.client.connection.connection import Connection


def handle_login(username: str, password: str):
    request = RequestFormat()
    request.command = cmd.LIST_MY_CHATS
    request[headers.USERNAME] = username
    request[headers.PASSWORD] = password
    conn = Connection()
    conn.send(request.build_header_message())
    conn.send(request.message)


class MainWindow(QMainWindow):
    def __init__(self, conv_db: ConvDB):
        super(MainWindow, self).__init__()
        self.conv_db = conv_db
        self.conversations = Conversations(self.conv_db)
        self.login = None
        self.register = None
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
        username = self.login.username
        password = self.login.password
        self.conv_db = ConvDB(username, password)
        handle_login(username, password)
        self.start_conversations_window()

    def start_login_window(self):
        self.login = Login()
        self.setCentralWidget(self.login)
        self.login.login.clicked.connect(self.login_user)
        self.login.register.clicked.connect(self.start_register_window)

    def start_register_window(self):
        self.register = Register()
        self.setCentralWidget(self.register)
        self.register.back.clicked.connect(self.start_login_window)
        self.register.register.clicked.connect(self.register_user)

    def register_user(self) -> None:
        if self.register.are_passwords_equal():
            self.start_login_window()
        else:
            self.register.clear_password()


app = QApplication(sys.argv)

conv_db = ConvDB('username')
window = MainWindow(conv_db)
window.show()
app.exec()