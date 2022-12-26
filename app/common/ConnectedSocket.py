import socket

BUFFER_SIZE = 4096
TIMEOUT_SECONDS = 1


class ConnectedSocket:
    """ Class for connected socket, is a wrapper for sending and receiving messages
        through a socket.

         send should be workable as is
         but recv will need a protocol built around it to check messages.
    """
    def __init__(self, connected_socket: socket.socket):
        self.socket = connected_socket
        self.socket.settimeout(TIMEOUT_SECONDS)

    def send(self, msg: str):
        # throws socket.error on failure to send the whole message
        converted_msg = bytes(msg, 'utf-8')
        self.socket.sendall(converted_msg)

    def recv(self, byte_count: int) -> bytes:
        # not guaranteed to get all the bytes, even if the number sent is lower than the byte_count
        return self.socket.recv(byte_count)

    def close(self):
        # closes socket and makes it completely unusable
        self.socket.close()
        self.socket = None
