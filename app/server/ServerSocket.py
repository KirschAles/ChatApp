import socket
from ..common.ConnectedSocket import ConnectedSocket

HOST = 'localhost'
PORT = 5000


def main():
    if socket.has_dualstack_ipv6():
        server_socket = socket.create_server((HOST, PORT), family=socket.AF_INET6, dualstack_ipv6=True)
    else:
        server_socket = socket.create_server((HOST, PORT))

    server_socket.listen()
    conn, addr = server_socket.accept()
    conn = ConnectedSocket(conn)
    msg = conn.recv(1024).decode()
    print(msg)


if __name__ == '__main__':
    main()
