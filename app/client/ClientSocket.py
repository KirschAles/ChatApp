import socket
from ..common.ConnectedSocket import ConnectedSocket

HOST = 'localhost'
PORT = 5000


def main():
    client_socket = ConnectedSocket(socket.create_connection((HOST, PORT)))
    client_socket.send('Hello World!')
    client_socket.close()


if __name__ == "__main__":
    main()
