import socket
from typing import TextIO

import app.common.request.request as request
from app.server.database.safedb import SafeDatabase


class ServerRequest(request.Request):
    headers_needed = []

    def __init__(self, reader: TextIO, db: SafeDatabase):
        super().__init__(reader)
        self.db = db
        self.build_request()
        if not self.has_all_headers():
            raise ValueError('Header missing.')

    def has_all_headers(self) -> bool:
        for header in self.headers_needed:
            if not (header in self.headers.keys()):
                return False
        return True

    def build_response(self):
        pass