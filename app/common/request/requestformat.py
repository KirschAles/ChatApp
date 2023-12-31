import socket
import app.common.headers as headers
import app.common.misc as misc
import app.common.clientcommands as cmd


class RequestFormat:
    def __init__(self):
        self.command = ''
        self._headers = {}
        self.message = ''
        self[headers.CONTENT_LENGTH] = str(len(bytes(self.message, encoding='utf-8')))

    def __setitem__(self, key: str, value: str):
        self._headers[key] = value

    def __getitem__(self, item: str):
        return self._headers[item]

    def build_header_message(self) -> str:
        msg = self.command + misc.LINE_END
        for key, value in self._headers.items():
            msg += key + misc.HEADER_DELIMETER + value + misc.LINE_END
        msg += misc.LINE_END
        return msg

    def build_structure(self, string: str):
        lines = string.split(misc.LINE_END)
        self.command = lines[0]
        for line in lines[1:]:
            if len(line) == 0:
                continue
            header = line.split(misc.HEADER_DELIMETER)
            self[header[0]] = header[1]

    def add_message(self, msg: str):
        self.message = msg
        self[headers.CONTENT_LENGTH] = str(len(bytes(msg, encoding='utf-8')))

    @property
    def success(self):
        return self.command != cmd.BAD

    @property
    def message_length(self) -> int:
        if headers.CONTENT_LENGTH in self._headers.keys():
            return int(self[headers.CONTENT_LENGTH])
        return 0

    def __str__(self):
        return self.build_header_message() + self.message