from app.server.database.dbsql import Database


class SafeDatabase:
    def __init__(self, db: Database):
        self.db = db

    def is_password_right(self, username, password) -> bool:
        return self.db.get_password(username) == password

    def belongs_to_chat(self, username, chat_id) -> bool:
        # chat's existence must be checked before calling this method
        return (username,) in self.db.get_chat_members(chat_id)

    def is_chat_id_valid(self, chat_id) -> bool:
        if self.db.get_chat_id(chat_id) == (chat_id,):
            return True
        return False

    def send_message(self, username, chat_id, message) -> None:
        if not self.is_chat_id_valid(chat_id):
            raise ValueError('Invalid chat_id.')
        if not self.belongs_to_chat(username, chat_id):
            raise ValueError('Not in chat.')
        self.db.insert_message(chat_id=chat_id,
                               sender_id=self.db.get_user_id(username),
                               message=message[:1024])

    def create_chat(self, username: str) -> int:
        return self.db.insert_chat(username)

    def add_to_chat(self, adder, chat_id, added) -> None:
        if not self.is_chat_id_valid(chat_id):
            raise ValueError('Invalid chat_id.')
        if not self.belongs_to_chat(adder, chat_id):
            raise ValueError('Cannot add to chat, you are not in.')

        self.db.insert_user_chat(added, chat_id)

    def create_user(self, username, password) -> None:
        return self.db.insert_user(username, password)

    def get_messages(self, chat_id, username) -> list:
        if not self.is_chat_id_valid():
            raise ValueError('Invalid chat_id.')
        if not self.belongs_to_chat(username, chat_id):
            raise ValueError('Not in chat.')
        return self.db.get_chat(chat_id)

    def get_users(self) -> list:
        return self.db.get_users()

    def get_my_chats(self) -> list:
        return self.db.get_my_chats()

    def get_chat_members(self, chat_id) -> list:
        return self.db.get_chat_members(chat_id)