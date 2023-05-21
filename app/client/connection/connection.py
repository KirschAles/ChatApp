import socket


HOST = 'localhost'
PORT = 5000
BUFFSIZE = 1024


class Connection:
    def __init__(self, host: str = HOST, port: int = PORT):
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._sock.connect((host, port))
        self.remainder = b''

    def send(self, msg: str) -> None:
        message = bytes(msg, 'utf-8')
        message_len = len(message)
        bytes_sent = 0
        while bytes_sent < message_len:
            print(bytes_sent)
            bytes_sent += self._sock.send(message[bytes_sent:])

    def recv_until(self, until: str) -> str:
        until_bytes = bytes(until, 'utf-8')
        message = self.remainder
        index = message.find(until_bytes)
        if index != -1:
            self.remainder = message[index+len(until_bytes):]
            return str(message[:index+len(until_bytes)])

        while True:
            new_part = self._sock.recv(BUFFSIZE)
            index = new_part.find(until_bytes)
            if index != -1:
                message += new_part[:index+len(until_bytes)]
                self.remainder = new_part[index+len(until_bytes):]
                break
            message += new_part
        return str(message)

    def recv_n_bytes(self, n):
        message = self.remainder[:min(n, len(self.remainder))]

        while len(message) < n:
            buffer = min(BUFFSIZE, n-len(message))
            message += self._sock.recv(buffer)

        self.remainder = self.remainder[min(len(message), len(self.remainder)):]
        return str(message)

    @property
    def writer(self):
        return self._sock.makefile('w')

    @property
    def reader(self):
        return self._sock.makefile('r')


