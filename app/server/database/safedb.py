from app.server.database.dbsql import Database
import app.common.headers as header


def message_to_dir(message: list) -> dir:
    message_dir = {header.SENDER_ID: message[0], header.TIME_SEND: message[1], header.MESSAGE: message[2]}
    return message_dir


class SafeDatabase:
    def __init__(self, db: Database):
        self.db = db

    def is_password_right(self, username: str, password: str) -> bool:
        return self.db.get_password(username) == password

    def belongs_to_chat(self, username: str, chat_id: int) -> bool:
        # chat's existence must be checked before calling this method
        return (username,) in self.db.get_chat_members(chat_id)

    def is_chat_id_valid(self, chat_id: int) -> bool:
        chat_id_test = self.db.get_chat_id(chat_id)
        if chat_id_test == chat_id:
            return True
        return False

    def send_message(self, username: str, chat_id: str, message: str) -> None:
        if not self.is_chat_id_valid(chat_id):
            raise ValueError('Invalid chat_id.')
        if not self.belongs_to_chat(username, chat_id):
            raise ValueError('Not in chat.')
        self.db.insert_message(chat_id=chat_id,
                               sender_id=self.db.get_user_id(username),
                               message=message[:1024])

    def create_chat(self, username: str) -> dir:
        chat_dir = {header.CHAT_ID: self.db.insert_chat(username)}
        return dir

    def add_to_chat(self, adder: str, chat_id: int, added: str) -> None:
        if not self.is_chat_id_valid(chat_id):
            raise ValueError('Invalid chat_id.')
        if not self.belongs_to_chat(adder, chat_id):
            raise ValueError('Cannot add to chat, you are not in.')

        self.db.insert_user_chat(added, chat_id)

    def create_user(self, username: str, password: str) -> dir:
        user_dir = {header.USER_ID: self.db.insert_user(username, password)}
        return user_dir

    def get_messages(self, chat_id: int, username: str) -> dir:
        if not self.is_chat_id_valid():
            raise ValueError('Invalid chat_id.')
        if not self.belongs_to_chat(username, chat_id):
            raise ValueError('Not in chat.')
        chat_msgs = self.db.get_chat(chat_id)
        messages = []
        for message in chat_msgs:
            messages.append(message_to_dir(message))
        return {header.MESSAGES: messages}

    def get_users(self) -> dir:
        users_dir = {header.USERS: self.db.get_users()}
        return users_dir

    def get_my_chats(self) -> dir:
        chats = {header.CHATS: self.db.get_my_chats()}
        return chats

    def get_chat_members(self, chat_id: int) -> dir:
        users_dir = {header.USERS: self.db.get_chat_members(chat_id)}
        return users_dir