from typing import TextIO
import app.common.headers as headers
import app.common.misc as misc
from app.client.connection.connection import ServerConnection


class Request:
    def __init__(self, conn: ServerConnection):
        self.conn = conn
        self.headers = {}
        self.buffer = []
        self.message = ''
        self.command = ''

    def build_header(self, line: str):
        header = line.split(misc.HEADER_DELIMETER)
        self.headers[header[0]] = header[1].strip()

    def build_headers(self):
        line = self.conn.recv_until(misc.LINE_END).strip(misc.LINE_END)
        while line != "":
            self.build_header(line)
            line = self.conn.recv_until(misc.LINE_END).strip(misc.LINE_END)

    def build_request(self):
        self.command = self.conn.recv_until(misc.LINE_END).strip(misc.LINE_END)
        self.build_headers()

    def read_message(self) -> str:
        return self.conn.recv_n_bytes(self.headers[headers.CONTENT_LENGTH])