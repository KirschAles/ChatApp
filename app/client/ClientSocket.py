import socket
from ..common.ConnectedSocket import ConnectedSocket

HOST = 'localhost'
PORT = 5000


def main():
    msg = input()
    while msg != 'exit()':
        client_socket = ConnectedSocket(socket.create_connection((HOST, PORT)))
        client_socket.send(msg)
        print(client_socket.recv(2048))
        client_socket.close()
        msg = input()


if __name__ == "__main__":
    main()
