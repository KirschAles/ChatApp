import socket
from .database.database import Database
from ..common.ConnectedSocket import ConnectedSocket

HOST = 'localhost'
PORT = 5000
BUFFER_SIZE = 4096
COMMAND_SIZE = 3

PUT = b'PUT'
GET = b'GET'
OK = 'OK'
db = Database()


def main():
    if socket.has_dualstack_ipv6():
        server_socket = socket.create_server((HOST, PORT), family=socket.AF_INET6, dualstack_ipv6=True)
    else:
        server_socket = socket.create_server((HOST, PORT))

    server_socket.listen()

    try:
        while True:
            conn = ConnectedSocket(server_socket.accept()[0])
            request_type = conn.recv(3)
            if request_type == GET:
                conn.send(OK)
                conn.send('\n')
                conn.send(db.update())
            elif request_type == PUT:
                db.insert(conn.recv(2048).decode())
                conn.send(OK)
                conn.send('\n')
            else:
                conn.send('BAD\n')
            conn.close()
    except KeyboardInterrupt:
        print("Ending Server.")


if __name__ == '__main__':
    main()
