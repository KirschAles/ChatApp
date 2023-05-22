"""
    These tests are made to controll the communication between client and server
    before the test is run, there must be already a server running on default host, port.
"""

from app.client.connection.server import Server





class TestServer:
    server = Server()
    username1 = "root"
    password1 = "toor"
    username2 = "admin"
    password2 = "admin"
    chat_id = None
    def test_register(self):
        assert self.server.register(self.username1, self.password1)
        assert self.server.register(self.username2, self.password2)

    def test_login(self):
        print(self.server.login(self.username1, self.password1))

    def test_create_chat(self):
        self.chat_id = self.server.create_chat()
        assert self.chat_id
        assert self.server.add_to_chat(self.username2, self.chat_id)
        print(self.server.get_chats())
