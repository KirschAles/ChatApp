"""
Module for interacting with the Server
"""
from app.client.connection.testconnection import Connection
from app.common.request.requestformat import RequestFormat
import app.common.headers as headers
import app.common.servercommands as cmd

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

    def get_request(self):
        request = RequestFormat()
        request[headers.USERNAME] = self.username
        request[headers.PASSWORD] = self.password
        return request

    def ready_communication(self):
        return self.get_connection(), self.get_request()

    def register(self, username: str, password: str):
        conn, request = self.ready_communication()
        request.command = cmd.REGISTER_USER

    def get_chats(self):
        conn, request = self.ready_communication()
        request.command = cmd.LIST_MY_CHATS

    def login(self, username: str, password: str):
        self.username = ""
        self.password = ""
        return self.get_chats()

    def create_chat(self):
        conn, request = self.ready_communication()
        request.command = cmd.CREATE_CHAT

    def add_to_chat(self, username: str, chat_id: int):
        conn, request = self.ready_communication()
        request.command = cmd.ADD_USER_TO_CHAT
        request[headers.TARGET_USERNAME] = username
        request[headers.CHAT_ID] = chat_id

    def create_chat_with(self, username: str):
        conn, request = self.ready_communication()
        chat_id = self.create_chat()
        self.add_to_chat(username, chat_id)

    def send_message(self, chat_id: int, msg: str):
        conn, request = self.ready_communication()
        request.command = cmd.SEND_MESSAGE
        request[headers.CHAT_ID] = chat_id

