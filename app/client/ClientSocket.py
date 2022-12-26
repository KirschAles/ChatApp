import socket

HOST = 'localhost'
PORT = 5000

client_socket = socket.create_connection((HOST, PORT))
client_socket.send('Hello World!')
client_socket.close()
