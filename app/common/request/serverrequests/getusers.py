from app.common.request.serverrequests.logged import LoggedRequest
from app.server.database.safedb import SafeDatabase
from typing import TextIO
import app.common.headers as headers


class GetUsers(LoggedRequest):
    headers_needed = []

    def __init__(self, reader: TextIO, db: SafeDatabase):
        super().__init__(reader, db)
        if not self.has_all_headers():
            raise ValueError('Missing headers')

    def execute(self):
        self.data_to_send.update(self.db.get_users())