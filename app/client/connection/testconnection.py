""" Connection class made for debugging,
    has the same interface as Connection, but interacts with terminal instead
"""


HOST = 'localhost'
PORT = 5000
BUFFSIZE = 1024


class Connection:
    def __init__(self, host: str = HOST, port: int = PORT):
        self.remainder = ""

    def send(self, msg: str) -> None:
        print(msg)

    def recv_until(self, until: str) -> str:
        message = self.remainder
        index = message.find(until)
        while index == -1:
            message += input()
            index = message.find(until)
        self.remainder = message[index + len(until):]
        return message[:index + len(until)]

    def recv_n_bytes(self, n):
        message = self.remainder
        while (len(message) < n):
            message += input()
        self.remainder = message[n:]
        return message[:n]
