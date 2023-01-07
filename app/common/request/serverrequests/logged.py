from app.common.request.serverrequest import ServerRequest
from app.server.database.safedb import SafeDatabase
from typing import TextIO
import app.common.headers as headers


class LoggedRequest(ServerRequest):
    headers_needed = []

    def __init__(self, reader: TextIO, db: SafeDatabase):
        super().__init__(reader, db)
        if not db.is_password_right(self.headers[headers.USERNAME], self.headers[headers.PASSWORD]):
            raise ValueError('Wrong username or password.')
