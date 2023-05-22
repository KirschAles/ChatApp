import socket
from typing import TextIO

import app.common.request.request as request
from app.server.database.safedb import SafeDatabase
import app.common.headers as headers
from app.common.request.response import Response
from app.common.clientcommands import OK


class ServerRequest(request.Request):
    headers_needed = [headers.USERNAME, headers.PASSWORD]

    def __init__(self, reader: TextIO, db: SafeDatabase):
        super().__init__(reader)
        self.return_message = []
        self.db = db
        self.build_request()

        self.headers_to_send = {}
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
        response = Response(self.reader, self.return_message)
        response.command = OK
        response.headers = self.headers_to_send.copy()
        response.build_response()
        response.send_response()