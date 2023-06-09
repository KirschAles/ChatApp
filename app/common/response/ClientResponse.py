from typing import TextIO
import json
import app.common.headers as header
from app.client.connection.connection import ServerConnection
from app.common.misc import LINE_END


class ClientResponse:
    def __init__(self):
        self.message = None
        self.conn = None
        self.headers = {}
        self.command = ''
        self.header_string = ''
        self.final_message = ''

    def add_writer(self, conn: ServerConnection):
        self.conn = conn

    @staticmethod
    def build_header_string(key, value):
        return key + ': ' + str(value) + LINE_END

    def build_response(self):
        self.message = str(json.dumps(self.headers))
        self.header_string = self.build_header_string(header.CONTENT_LENGTH, len(bytes(self.message, encoding='utf-8')))
        self.header_string += LINE_END

    def send_response(self):
        print(self.command + LINE_END)
        print(self.header_string)
        print(self.message)
        self.conn.send(self.command + LINE_END)
        self.conn.send(self.header_string)
        self.conn.send(self.message)