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
    def _load_script(path: str):
        file = open(path, 'r', encoding='utf-8')
        script = file.read()
        file.close()
        print(script)
        return script

    def insert_user(self, username: str, password: str):
        self.cursor.execute(script.INSERT_USER.format(username, password))

    def get_username(self, user_id: int):
        self.cursor.execute(script.GET_USERNAME.format(user_id))
        return self.cursor.fetchone()[0]

    def get_chat(self, chat_id: int):
        self.cursor.execute(script.GET_CHAT.format(chat_id))
        return self.cursor.fetchall()

    def insert_message(self, chat_id: int, sender_id: int, message: str):
        self.cursor.execute(script.INSERT_MESSAGE.format(chat_id, sender_id, message))

    def _insert_user_chat(self, user_id: int, chat_id: int):
        self.cursor.execute(script.INSERT_USER_CHAT.format(user_id, chat_id))

    def insert_chat(self, user_ids: list):
        self.cursor.execute(script.INSERT_CHAT)
        chat_id = self.cursor.fetchone()[0]
        for user_id in user_ids:
            self._insert_user_chat(user_id, chat_id)
        return chat_id

    def get_chats(self):
        self.cursor.execute(script.GET_CHATS)
        return self.cursor.fetchall()

    def get_users(self):
        self.cursor.execute(script.GET_USERS)
        return self.cursor.fetchall()

    def get_messages(self):
        self.cursor.execute(script.GET_MESSAGES)
        return self.cursor.fetchall()

    def get_user_chats(self):
        self.cursor.execute(script.GET_USER_CHATS)
        return self.cursor.fetchall()

if __name__ == '__main__':
    Database()