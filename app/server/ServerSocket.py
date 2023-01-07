import socket
from typing import TextIO

from app.server.database.dbsql import Database

HOST = 'localhost'
PORT = 5000
BUFFER_SIZE = 4096

db = Database()


def handle_request(reader: TextIO):
    command = reader.readline(40).strip('\n').strip('\r')


def main():
    if socket.has_dualstack_ipv6():
        server_socket = socket.create_server((HOST, PORT), family=socket.AF_INET6, dualstack_ipv6=True)
    else:
        server_socket = socket.create_server((HOST, PORT))

    server_socket.listen()

    try:
        while True:
            conn = server_socket.accept()[0]
            reader = conn.makefile('rw', buffering=BUFFER_SIZE, encoding='utf8')
            handle_request(reader)
            conn.close()
    except KeyboardInterrupt:
        print("Ending Server.")


if __name__ == '__main__':
    main()
