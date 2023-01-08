from typing import TextIO

import app.common.headers as headers


class Response:
    def __init__(self, writer: TextIO, message=None):
        if message is None:
            message = []
        self.writer = writer
        self.message = message
        self.headers = {}
        self.command = ''

        self.header_string = ''
        self.final_message = ''

    @staticmethod
    def build_header_string(key, value):
        return key + ': ' + str(value) + '\n'

    def build_header_strings(self):
        for key, value in self.headers.items():
            self.header_string += self.build_header_string(key, value)
        self.header_string += '\n'

    def build_message(self):
        long_message = ''
        for part in self.message[0: len(self.message) - 1]:
            long_message += str(part)
            long_message += '+'
        long_message += self.message[-1]
        self.headers[headers.CONTENT_LENGTH] = len(long_message)
        self.final_message = long_message

    def build_response(self):
        self.build_header_strings()
        self.build_message()

    def send_response(self):
        self.writer.write(self.command)
        self.writer.write(self.header_string)
        self.writer.write(self.final_message)
