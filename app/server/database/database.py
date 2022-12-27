class Database:
    def __init__(self):
        self.db = []

    def insert(self, msg: str):
        self.db.append(msg)

    def update(self) -> str:
        return '\n'.join(self.db)
