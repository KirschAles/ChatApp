from typing import TextIO

import app.common.headers as headers
from app.common.response.ClientResponse import ClientResponse


class Response(ClientResponse):
    def __init__(self, writer: TextIO, message: list):
        super().__init__(message)
        self.writer = writer

    def build_message(self):
        long_message = ''
        if len(self.message) != 0:
            for part in self.message[0: len(self.message) - 1]:
                long_message += str(part)
                long_message += '+'
            long_message += self.message[-1]
        self.headers[headers.CONTENT_LENGTH] = len(long_message)
        self.final_message = long_message

