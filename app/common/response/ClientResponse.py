from typing import TextIO


class ClientResponse:
    def __init__(self, message: list):
        self.message = message
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

    def build_header_strings(self):
        for key, value in self.headers.items():
            self.header_string += self.build_header_string(key, value)
        self.header_string += '\n'

    def build_message(self):
        for part in self.message:
            self.final_message += str(part)

    def build_response(self):
        self.build_message()
        self.build_header_strings()

    def send_response(self):
        self.writer.write(self.command + "\n")
        self.writer.write(self.header_string)
        self.writer.write(self.final_message)