from app.common.request.serverrequests.logged import LoggedRequest
from app.server.database.safedb import SafeDatabase
from typing import TextIO
import app.common.headers as headers


class AddToChat(LoggedRequest):
    headers_needed = [headers.CHAT_ID, headers.TARGET_USERNAME]

    def __init__(self, reader: TextIO, db: SafeDatabase):
        super().__init__(reader, db)
        if not self.has_all_headers():
            raise ValueError('Missing headers')

    def execute(self):
        adder = self.headers[headers.USERNAME]
        added = self.headers[headers.TARGET_USERNAME]
        chat_id = self.headers[headers.CHAT_ID]
        self.db.add_to_chat(adder, chat_id, added)