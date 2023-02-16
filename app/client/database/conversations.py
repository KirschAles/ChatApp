from app.client.database.chat import ChatDB


class ConvDB:
    def __init__(self, username: str):
        self._chats = {}
        self._username = username

    def __getitem__(self, id: int):
        return self._chats[id]

    def __setitem__(self, id: int, users: list):
        self._chats[id] = ChatDB(id)
        self._chats[id].add_user(self.username)
        for user in users:
            self._chats[id].add_user(user)

    def __iter__(self):
        return self._chats.values().__iter__()

    def next_id(self) -> int:
        return len(self._chats)

    @property
    def username(self):
        return self._username