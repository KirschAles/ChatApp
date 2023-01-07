from app.common.request.serverrequest import ServerRequest
from app.server.database.safedb import SafeDatabase
from typing import TextIO
import app.common.headers as headers


class RegisterRequest(ServerRequest):
    headers_needed = []

    def __init__(self, reader: TextIO, db: SafeDatabase):
        super().__init__(reader, db)

    def execute(self):
        self.db.create_user(self.headers[headers.USERNAME], self.headers[headers.PASSWORD])
