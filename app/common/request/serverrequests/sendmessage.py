from app.common.request.serverrequests.logged import LoggedRequest
from app.server.database.safedb import SafeDatabase
from typing import TextIO
import app.common.headers as headers


class SendMessageRequest(LoggedRequest):
    headers_needed = [headers.CHAT_ID, headers.CONTENT_LENGTH]

    def __init__(self, reader: TextIO, db: SafeDatabase):
        self.super(self).__init__(reader, db)
        if not self.has_all_headers():
            raise ValueError('Missing headers')
