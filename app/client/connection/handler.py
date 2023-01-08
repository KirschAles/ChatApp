import socket

from app.common.request.request import Request
from app.common.response.ClientResponse import ClientResponse
from app.common.headers import CONTENT_LENGTH, USERNAME, PASSWORD

HOST = 'localhost'
PORT = 5000
username = ''
password = ''


def handle_response(response: ClientResponse):
    response.build_message()
    response.headers[CONTENT_LENGTH] = len(response.final_message)
    response.headers[USERNAME] = username
    response.headers[PASSWORD] = password
    response.build_header_strings()
    conn = socket.create_connection((HOST, PORT))
    writer = conn.makefile('rw', encoding='utf8')
    response.add_writer(writer)
    response.send_response()

    request = Request(writer)
    request.build_request()
    request.read_message()
    conn.close()
    return request