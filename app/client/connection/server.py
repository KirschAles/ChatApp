"""
Module for interacting with the Server
"""
from testconnection import Connection

HOST = 'localhost'
PORT = 5000
BUFF_SIZE = 1024


class Server:
    def __init__(self, host: str = HOST, port: int = PORT, buffer_size: int = BUFF_SIZE):
        self.host = host
        self.port = port
        self.buffer_size = buffer_size

        # will saved here
        # so all calls dont have to include username and password in parameters
        self.username = ""
        self.password = ""

    def get_connection(self):
        return Connection(self.host, self.port)

    def register(self, username: str, password: str):
        conn = self.get_connection()

    def get_chats(self):
        conn = self.get_connection()

    def login(self, username: str, password: str):
        self.username = ""
        self.password = ""
        return self.get_chats()

    def create_chat(self):
        conn = self.get_connection()

    def add_to_chat(self, username: str, chat_id: int):
        conn = self.get_connection()

    def create_chat_with(self, username: str):
        conn = self.get_connection()

    def send_message(self, chat_id: int, msg: str):
        conn = self.get_connection()


