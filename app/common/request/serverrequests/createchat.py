from app.common.request.serverrequests.logged import LoggedRequest
from app.server.database.safedb import SafeDatabase
from typing import TextIO
import app.common.headers as headers


class CreateChat(LoggedRequest):
    headers_needed = []

    def __init__(self, reader: TextIO, db: SafeDatabase):
        super().__init__(reader, db)
        if not self.has_all_headers():
            raise ValueError('Missing headers')

    def execute(self):
        self.headers_to_send[headers.CHAT_ID] = self.db.create_chat(self.headers[headers.USERNAME])