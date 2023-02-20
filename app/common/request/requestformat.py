import socket


class RequestFormat:
    def __init__(self):
        self.command = ''
        self._headers = {}
        self.message = ''

    def __setitem__(self, key: str, value: str):
        self._headers[key] = value

    def __getitem__(self, item: str):
        return self._headers[item]

    def build_header_message(self) -> str:
        msg = self.command + '\n'
        for key, value in self._headers.items():
            msg += key + ': ' + value + '\n'
        msg += '\n'
        return msg