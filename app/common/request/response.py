from typing import TextIO

import app.common.headers as headers
from app.common.response.ClientResponse import ClientResponse
from app.client.connection.connection import ServerConnection


class Response(ClientResponse):
    def __init__(self, conn: ServerConnection):
        super().__init__()
        self.conn = conn

