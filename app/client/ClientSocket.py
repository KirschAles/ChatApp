import socket
from ..common.ConnectedSocket import ConnectedSocket

HOST = 'localhost'
PORT = 5000

client_socket = ConnectedSocket(socket.create_connection((HOST, PORT)))
client_socket.send('Hello World!')
client_socket.close()
