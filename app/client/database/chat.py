import datetime
from app.client.connection.server import Server


class Message:
    def __init__(self, text: str, sender: str, time: datetime.datetime):
        self._text = text
        self._time = time
        self._sender = sender

    @property
    def text(self) -> str:
        return self._text

    @property
    def time(self) -> datetime.datetime:
        return self._time

    @property
    def sender(self) -> str:
        return self._sender

    def __gt__(self, other) -> bool:
        return self.time > other.time

    def __lt__(self, other) -> bool:
        return self.time < other.time

    def __str__(self) -> str:
        return self.sender + ': ' + self.text


class ChatDB:
    def __init__(self, chat_id: int, server: Server):
        self._id = chat_id
        self._users = []
        self._messages = []
        self._server = server

    def add_message(self, text: str, sender: str) -> None:
        time = datetime.datetime.now()
        message = Message(text, sender, time)
        self._server.send_message(self._id, text)
        self._messages.append(message)
        self._messages.sort(reverse=True)

    @property
    def last_message(self) -> str:
        return self._messages[0]

    @property
    def messages(self) -> list:
        return self._server.get_messages(self._id)

    def add_user(self, username: str):
        self._server.add_to_chat(username, self._id)

    @property
    def users(self) -> list:
        return self._server.get_users()

    @property
    def id(self) -> int:
        return self._id