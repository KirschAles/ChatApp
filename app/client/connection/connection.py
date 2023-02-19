import socket


HOST = 'localhost'
PORT = 5000


class Connection:
    def __init__(self, host: str = HOST, port: int = PORT):
        self._sock = socket.create_connection((host, port))

    @property
    def writer(self):
        return self._sock.makefile('w', encoding='utf8')

    @property
    def reader(self):
        return self._sock.makefile('r', encoding='utf8')



