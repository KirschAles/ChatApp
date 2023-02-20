"""
PORT PRINTER

prints all data on the port to the console,
made for checking of connection data
"""
import socket
from time import sleep

PORT = 5000

sock = socket.socket()
sock.bind(('localhost', PORT))
sock.listen()
while 42:
    conn, random = sock.accept()
    print(conn.recv(1024))

    conn.close()

