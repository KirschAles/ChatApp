from typing import TextIO
import json
import app.common.headers as header


class ClientResponse:
    def __init__(self):
        self.message = None
        self.writer = None
        self.headers = {}
        self.command = ''
        self.header_string = ''
        self.final_message = ''

    def add_writer(self, writer: TextIO):
        self.writer = writer

    @staticmethod
    def build_header_string(key, value):
        return key + ': ' + str(value) + '\n'

    def build_response(self):
        self.message = str(json.dumps(self.headers))
        self.header_string = self.build_header_string(header.CONTENT_LENGTH, len(bytes(self.message, encoding='utf-8')))
        self.header_string += '\n'*2

    def send_response(self):
        self.writer.write(self.command + "\n")
        self.writer.write(self.header_string)
        self.writer.write(self.message)