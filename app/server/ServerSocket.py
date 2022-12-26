import socket

HOST = 'localhost'
PORT = 5000


if socket.has_dualstack_ipv6():
    server_socket = socket.create_server((HOST, PORT), family=socket.AF_INET6, dualstack_ipv6=True)
else:
    server_socket = socket.create_server((HOST, PORT))

server_socket.listen()
conn, addr = server_socket.accept()

msg = conn.recv(1024)
print(msg)