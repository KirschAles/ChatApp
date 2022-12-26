import socket

HOST = 'localhost'
PORT = 5000

client_socket = socket.create_connection((HOST, PORT))
client_socket.send(b'Hello World!')
client_socket.close()
