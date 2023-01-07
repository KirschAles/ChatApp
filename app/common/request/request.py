from typing import TextIO
import socket


class Request:
    def __init__(self, reader: TextIO):
        self.reader = reader
        self.headers = {}
        self.buffer = []

    def build_header(self, line: str):
        header = line.split(':')
        self.headers[header[0]] = header[1].strip()

    def build_headers(self):
        line = self.reader.readline().strip('\n').strip('\r')
        while line:
            self.build_header(line)

    def build_request(self):
        self.command = self.reader.readline().strip('\n').strip('\r')
        self.build_headers()
