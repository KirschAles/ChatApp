import psycopg2


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
        cursor = self.conn.cursor()
        cursor.execute(self._load_script(delete_path))
        cursor.execute(self._load_script(create_path))

    @staticmethod
    def _load_script(path: str):
        script = ''
        with open(path, 'r', encoding='utf-8') as file:
            script = file.read()
        return script


if __name__ == '__main__':
    Database()