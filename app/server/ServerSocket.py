import socket
from typing import TextIO
from app.server.database.dbsql import Database
from app.server.database.safedb import SafeDatabase
import app.common.servercommands as cmd
from app.common.request.serverrequests.register import RegisterRequest
from app.common.request.serverrequests.getusers import GetUsers
from app.common.request.serverrequests.addtochat import AddToChat
from app.common.request.serverrequests.sendmessage import SendMessageRequest
from app.common.request.serverrequests.createchat import CreateChat
from app.common.request.serverrequests.getchatusers import GetChatUsers
from app.common.request.serverrequests.getmessages import GetMessages
from app.common.request.serverrequests.getmychats import GetMyChats

HOST = 'localhost'
PORT = 5000
BUFFER_SIZE = 4096


db = SafeDatabase(Database())


def get_request(command: str, reader: TextIO):
    if command == cmd.REGISTER_USER:
        return RegisterRequest(reader, db)
    if command == cmd.LIST_USERS:
        return GetUsers(reader, db)
    if command == cmd.SEND_MESSAGE:
        return SendMessageRequest(reader, db)
    if command == cmd.LIST_MESSAGES_IN_CHAT:
        return GetMessages(reader, db)
    if command == cmd.LIST_MY_CHATS:
        return GetMyChats(reader, db)
    if command == cmd.LIST_USERS_IN_CHAT:
        return GetChatUsers(reader, db)
    if command == cmd.ADD_USER_TO_CHAT:
        return AddToChat(reader, db)
    if command == cmd.CREATE_CHAT:
        return CreateChat(reader, db)


def handle_request(reader: TextIO):
    command = reader.readline(40).strip('\n').strip('\r')
    request = get_request(command, reader)
    request.build_request()
    request.execute()
    request.send_response()


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
            reader.close()
            conn.close()
    except KeyboardInterrupt:
        print("Ending Server.")


if __name__ == '__main__':
    main()
