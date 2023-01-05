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


if __name__ == '__main__':
    Database()