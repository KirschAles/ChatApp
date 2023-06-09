from PyQt5.QtWidgets import QVBoxLayout, QPushButton, QTextEdit, QButtonGroup, QWidget
from app.client.database.conversations import ConvDB
from app.client.gui.widgets import TextWithButton


class Conversations(QWidget):
    def __init__(self, conv_db: ConvDB):
        super().__init__()
        self.setLayout(QVBoxLayout())
        self._db = conv_db
        self._conv_widgets = {}
        self.add_conv = TextWithButton('Add conversation')
        self.add_conv.button.clicked.connect(self.new_conversation)
        self.layout().addWidget(self.add_conv)
        self.chat_buttons = QButtonGroup()
        self.load_chats()

    def new_conversation(self):
        new_id = self._db.create_chat() # temprorary, will later be found by request to server
        self._db[new_id] = [self.add_conv.text()]
        self.add_conv.clear()
        self.update_widget(new_id)
        self.layout().addWidget(self._conv_widgets[new_id])

    def update_widget(self, chat_id: int):
        button = QPushButton(str(self._db[chat_id].users))
        self.chat_buttons.addButton(button, chat_id)
        self._conv_widgets[chat_id] = button

    def load_chats(self):
        self._db.update()
        for chat in self._db:
            button = QPushButton(str(chat.users))
            self.layout().addWidget(button)
            self.chat_buttons.addButton(button, chat.id)
            self._conv_widgets[chat.id] = button