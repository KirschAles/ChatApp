import psycopg2
import app.server.database.scripts.sql as script


class Database:
    def __init__(self,
                 name: str = 'chat_db',
                 user: str = 'chat_user',
                 password: str = 'chat_user',
                 create_path: str = 'app/server/database/scripts/CREATE.sql',
                 delete_path: str = 'app/server/database/scripts/DELETE.sql',
                 host: str = 'localhost',
                 port: str = '5432'):
        self.conn = psycopg2.connect(
            database=name, user=user, password=password, host=host, port=port
        )
        self.cursor = self.conn.cursor()
        self.cursor.execute(self._load_script(delete_path))
        self.cursor.execute(self._load_script(create_path))

    @staticmethod
    def _load_script(path: str) -> str:
        file = open(path, 'r', encoding='utf-8')
        scrip = file.read()
        file.close()
        return scrip

    def insert_user(self, username: str, password: str) -> int:
        self.cursor.execute(script.INSERT_USER.format(username, password))
        return self.cursor.fetchone()[0]

    def get_username(self, user_id: int) -> str:
        self.cursor.execute(script.GET_USERNAME.format(user_id))
        username = self.cursor.fetchone()
        if username is None:
            raise ValueError('Nonexistent user_id.')
        return username[0]

    def get_user_id(self, username: str) -> int:
        self.cursor.execute(script.GET_USER_ID.format(username))
        user_id = self.cursor.fetchone()
        if user_id is None:
            raise ValueError("User doesn't exist")
        return user_id[0]

    def get_password(self, username: str) -> str:
        self.cursor.execute(script.GET_PASSWORD.format(username))
        password = self.cursor.fetchone()
        if password is None:
            raise ValueError("Username doesn't exist.")
        return password[0]

    def get_chat_id(self, chat_id: int) -> int:
        self.cursor.execute(script.GET_CHAT_ID.format(chat_id))
        chat_id = self.cursor.fetchone()
        if chat_id is None:
            return ValueError("chat doesn't exit.")
        return chat_id[0]

    def get_chat_members(self, chat_id: int) -> list:
        self.cursor.execute(script.GET_CHAT_MEMBERS.format(chat_id))
        chat_members = self.cursor.fetchall()
        return chat_members

    def get_chat(self, chat_id: int) -> list:
        self.cursor.execute(script.GET_CHAT.format(chat_id))
        return self.cursor.fetchall()

    def insert_message(self, chat_id: int, sender_id: int, message: str) -> None:
        self.cursor.execute(script.INSERT_MESSAGE.format(chat_id, sender_id, message))

    def insert_user_chat(self, username: str, chat_id: int) -> None:
        user_id = self.get_user_id(username)
        self.cursor.execute(script.INSERT_USER_CHAT.format(user_id, chat_id))

    def insert_chat(self, username: str) -> int:
        self.cursor.execute(script.INSERT_CHAT)
        chat_id = self.cursor.fetchone()[0]
        self.insert_user_chat(username, chat_id)
        return chat_id

    def get_chats(self) -> list:
        self.cursor.execute(script.GET_CHATS)
        chats = self.cursor.fetchall()
        return chats

    def get_users(self) -> list:
        self.cursor.execute(script.GET_USERS)
        users = self.cursor.fetchall()
        return users

    def get_messages(self) -> list:
        self.cursor.execute(script.GET_MESSAGES)
        messages = self.cursor.fetchall()
        return messages

    def get_user_chats(self) -> list:
        self.cursor.execute(script.GET_USER_CHATS)
        chats = self.cursor.fetchall()
        return chats

    def get_my_chats(self) -> list:
        self.cursor.execute(script.GET_MY_CHATS)
        return self.cursor.fetchall()


if __name__ == '__main__':
    Database()