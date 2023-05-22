from app.common.request.serverrequests.logged import LoggedRequest
from app.server.database.safedb import SafeDatabase
from typing import TextIO
import app.common.headers as headers


class GetMessages(LoggedRequest):
    headers_needed = [headers.CHAT_ID]

    def __init__(self, reader: TextIO, db: SafeDatabase):
        super().__init__(reader, db)
        if not self.has_all_headers():
            raise ValueError('Missing headers')

    def execute(self):
        self.return_message = self.db.get_messages(int(self.headers[headers.CHAT_ID]), self.headers[headers.USERNAME])