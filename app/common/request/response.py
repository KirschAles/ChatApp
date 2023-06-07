from typing import TextIO

import app.common.headers as headers
from app.common.response.ClientResponse import ClientResponse


class Response(ClientResponse):
    def __init__(self, writer: TextIO):
        super().__init__()
        self.writer = writer

