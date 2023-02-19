from typing import TextIO


class RequestFormat:
    def __init__(self):
        self.command = ''
        self._headers = {}
        self.message = ''

    def __setitem__(self, key: str, value: str):
        self._headers[key] = value

    def __getitem__(self, item: str):
        return self._headers[item]

    def send(self, writer: TextIO):
        writer.write(self.command + '\n')
        for key, value in self._headers:
            writer.write(key + ': ' + value + '\n')
        writer.write('\n')
        writer.write(self.message)
