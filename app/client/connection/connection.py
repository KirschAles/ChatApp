import socket


HOST = 'localhost'
PORT = 5000
BUFFSIZE = 1024


class Connection:
    def __init__(self):
        self._sock = None
        self.remainder = b''

    def send(self, msg: str) -> None:
        print(msg)
        message = bytes(msg, 'utf-8')
        message_len = len(message)
        bytes_sent = 0
        while bytes_sent < message_len:
            bytes_sent += self._sock.send(message[bytes_sent:])

    def recv_until(self, until: str) -> str:
        until_bytes = bytes(until, 'utf-8')
        message = self.remainder
        print(until_bytes)
        index = message.find(until_bytes)
        while index == -1:
            message += self._sock.recv(BUFFSIZE)
            index = message.find(until_bytes)
            print(message)
            print(until_bytes)
            print(index)
        self.remainder = message[index + len(until_bytes):]
        print(self.remainder)
        return str(message[:index + len(until_bytes)], 'utf-8')

    def recv_n_bytes(self, n):
        message = self.remainder
        while len(message) < n:
            buffer = min(BUFFSIZE, n-len(message))
            message += self._sock.recv(buffer)

        self.remainder = message[n:]
        print(self.remainder)
        return str(message[:n], 'utf-8')

    @property
    def writer(self):
        return self._sock.makefile('w')

    @property
    def reader(self):
        return self._sock.makefile('r')


class ClientConnection(Connection):
    def __init__(self, host: str = HOST, port: int = PORT):
        super().__init__()
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._sock.connect((host, port))


class ServerConnection(Connection):
    def __init__(self, sock: socket.socket):
        super().__init__()
        self._sock = sock
