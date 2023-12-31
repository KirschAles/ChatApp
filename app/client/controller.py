import socket
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
from app.client.connection.server import Server


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.server = Server()
        self.conv_db = ConvDB(self.server)
        self.conversations = None
        self.login = None
        self.register = None
        self.start_login_window()

    def handle_login(self, username: str, password: str) -> bool:
        return self.server.login(username, password)

    def handle_register(self, username: str, password: str):
        return self.server.register(username, password)

    def start_conversations_window(self):
        print("start conversation window")
        self.conversations = Conversations(self.conv_db)
        print("conversation window started")
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
        self.handle_login(username, password)
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
            self.handle_register(self.register.username(), self.register.password())
            self.start_login_window()
        else:
            self.register.clear_password()


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()