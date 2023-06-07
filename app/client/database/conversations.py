from app.client.database.chat import ChatDB
from app.client.connection.server import Server


class ConvDB:
    def __init__(self, server: Server):
        self._chats = {}
        self._server = server

    def __getitem__(self, id: int):
        return self._chats[id]

    def __setitem__(self, id: int, users: list):
        self._chats[id] = ChatDB(id, self._server)
        for user in users:
            self._chats[id].add_user(user)

    def __iter__(self):
        return self._chats.values().__iter__()

    def next_id(self) -> int:
        return self._server.create_chat()

    @property
    def username(self):
        return self._server.username

    @property
    def password(self):
        return self._server.password