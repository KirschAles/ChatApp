from chat import ChatDB


class ConvDB:
    def __init__(self):
        self._chats = {}

    def __getitem__(self, id: int):
        return self._chats[id]

    def __setitem__(self, id: int, users: list):
        self._chats[id] = ChatDB(id)
        for user in users:
            self._chats[id].add_user(user)
