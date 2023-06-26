from app.client.database.chat import ChatDB
from app.client.connection.server import Server


class ConvDB:
    def __init__(self, server: Server):
        self._chats = {}
        self._server = server

    def __getitem__(self, chat_id: int):
        return self._chats[chat_id]

    def __setitem__(self, chat_id: int, users: list):
        for user in users:
            self._chats[chat_id].add_user(user)

    def __iter__(self):
        return self._chats.values().__iter__()

    def create_chat(self) -> int:
        chat_id = self._server.create_chat()
        self._chats[chat_id] = ChatDB(chat_id, self._server)
        return chat_id

    @property
    def username(self):
        return self._server.username

    @property
    def password(self):
        return self._server.password

    def update(self):
        chats = self._server.get_chats()
        print(chats)