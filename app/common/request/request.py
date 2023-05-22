from typing import TextIO
import app.common.headers as headers
import app.common.misc as misc

class Request:
    def __init__(self, reader: TextIO):
        self.reader = reader
        self.headers = {}
        self.buffer = []
        self.message = ''
        self.command = ''

    def build_header(self, line: str):
        header = line.split(misc.HEADER_DELIMETER)
        self.headers[header[0]] = header[1].strip()

    def build_headers(self):
        line = self.reader.readline().strip('\n').strip('\r')
        while line != "":
            self.build_header(line)
            line = self.reader.readline().strip('\n').strip('\r')

    def build_request(self):
        self.command = self.reader.readline().strip('\n').strip('\r')
        self.build_headers()

    def read_message(self) -> str:
        return self.reader.read(self.headers[headers.CONTENT_LENGTH])