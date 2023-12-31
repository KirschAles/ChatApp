import socket
from typing import TextIO

import app.common.request.request as request
from app.server.database.safedb import SafeDatabase
import app.common.headers as headers
from app.common.request.response import Response
from app.common.clientcommands import OK
from app.client.connection.connection import ServerConnection

class ServerRequest(request.Request):
    headers_needed = [headers.USERNAME, headers.PASSWORD]

    def __init__(self, conn: ServerConnection, db: SafeDatabase):
        super().__init__(conn)
        self.return_message = []
        self.db = db
        self.build_request()

        self.data_to_send = {}
        if not self.has_all_headers():
            raise ValueError('Header missing.')

    def has_all_headers(self) -> bool:
        for header in self.headers_needed:
            if not (header in self.headers.keys()):
                return False
        return True

    def execute(self):
        pass

    def send_response(self):
        response = Response(self.conn)
        response.command = OK
        response.headers = self.data_to_send
        response.build_response()
        print(self.data_to_send)
        response.send_response()