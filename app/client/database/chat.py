import datetime


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
    def __init__(self, chat_id: int):
        self._id = chat_id
        self._users = []
        self._messages = []

    def add_message(self, text: str, sender: str, time: datetime.datetime = datetime.datetime.now()) -> None:
        message = Message(text, sender, time)
        self._messages.append(message)
        self._messages.sort(reverse=True)

    @property
    def last_message(self) -> str:
        return self._messages[0].text

    @property
    def messages(self) -> list:
        return self._messages

    def add_user(self, username: str):
        self._users.append(username)

    @property
    def users(self) -> list:
        return self._users

    @property
    def id(self) -> int:
        return self._id