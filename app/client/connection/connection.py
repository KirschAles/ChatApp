import socket


HOST = 'localhost'
PORT = 5000


class Connection:
    def __init__(self, host: str = HOST, port: int = PORT):
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._sock.connect((host, port))

    def send(self, msg: str) -> None:
        message = bytes(msg, 'utf-8')
        message_len = len(message)
        bytes_sent = 0
        while bytes_sent < message_len:
            print(bytes_sent)
            bytes_sent += self._sock.send(message[bytes_sent:])

    @property
    def writer(self):
        return self._sock.makefile('w')

    @property
    def reader(self):
        return self._sock.makefile('r')



