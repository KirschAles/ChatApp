"""
Module for interacting with the Server
"""
from app.client.connection.connection import Connection
from app.common.request.requestformat import RequestFormat
import app.common.headers as headers
import app.common.servercommands as cmd
import app.common.misc as misc

HOST = 'localhost'
PORT = 5000
BUFF_SIZE = 1024


def send_request(conn: Connection, request: RequestFormat) -> None:
    conn.send(request.build_header_message())
    conn.send(request.message)


def recv_response(conn: Connection) -> RequestFormat:
    response = RequestFormat()
    response.build_structure(conn.recv_until(misc.LINE_END*2))
    response.msg = conn.recv_n_bytes(int(response[headers.CONTENT_LENGTH]))
    return response


class Server:
    def __init__(self, host: str = HOST, port: int = PORT, buffer_size: int = BUFF_SIZE):
        self.host = host
        self.port = port
        self.buffer_size = buffer_size

        # will saved here
        # so all calls dont have to include username and password in parameters
        self.username = ""
        self.password = ""

    def get_connection(self) -> Connection:
        return Connection(self.host, self.port)

    def init_request(self) -> RequestFormat:
        request = RequestFormat()
        request[headers.USERNAME] = self.username
        request[headers.PASSWORD] = self.password
        return request

    def ready_communication(self) -> (Connection, RequestFormat):
        return self.get_connection(), self.init_request()

    def register(self, username: str, password: str):
        conn, request = self.ready_communication()
        request.command = cmd.REGISTER_USER
        request[headers.USERNAME] = username
        request[headers.PASSWORD] = password
        send_request(conn, request)
        response = recv_response(conn)
        return response.success

    def get_chats(self) -> str:
        conn, request = self.ready_communication()
        request.command = cmd.LIST_MY_CHATS
        send_request(conn, request)
        response = recv_response(conn)
        if response.success:
            return response.message
        raise Exception()

    def login(self, username: str, password: str) -> str:
        self.username = username
        self.password = password
        return self.get_chats()

    def create_chat(self) -> int:
        conn, request = self.ready_communication()
        request.command = cmd.CREATE_CHAT
        send_request(conn, request)
        response = recv_response(conn)
        if response.success:
            return int(response[headers.CHAT_ID])
        raise Exception()

    def add_to_chat(self, username: str, chat_id: int) -> bool:
        conn, request = self.ready_communication()
        request.command = cmd.ADD_USER_TO_CHAT
        request[headers.TARGET_USERNAME] = username
        request[headers.CHAT_ID] = str(chat_id)
        send_request(conn, request)
        response = recv_response(conn)
        return response.success

    def create_chat_with(self, username: str) -> int:
        conn, request = self.ready_communication()
        chat_id = self.create_chat()
        self.add_to_chat(username, chat_id)
        send_request(conn, request)
        response = recv_response(conn)
        if response.success:
            return int(response[headers.CHAT_ID])
        raise Exception

    def send_message(self, chat_id: int, msg: str) -> bool:
        conn, request = self.ready_communication()
        request.command = cmd.SEND_MESSAGE
        request[headers.CHAT_ID] = str(chat_id)
        request.add_message(msg)
        send_request(conn, request)
        response = recv_response(conn)
        return response.success


