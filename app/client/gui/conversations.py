from PyQt5.QtWidgets import QVBoxLayout, QPushButton, QTextEdit, QButtonGroup, QWidget
from app.client.database.conversations import ConvDB


class Conversations(QWidget):

    def __init__(self, conv_db: ConvDB = ConvDB()):
        super().__init__()
        self.setLayout(QVBoxLayout())
        self._db = conv_db
        self._conv_widgets = {}
        add_conv = QPushButton('Add conversation')
        add_conv.clicked.connect(self.new_conversation)
        self.username_field = QTextEdit()
        self.layout().addWidget(add_conv)
        self.layout().addWidget(self.username_field)
        self.chat_buttons = QButtonGroup()
        self.load_chats()

    def new_conversation(self):
        new_id = self._db.next_id() # temprorary, will later be found by request to server
        self._db[new_id] = [self.username_field.toPlainText()]
        self.username_field.setText('')
        self.update_widget(new_id)
        self.layout().addWidget(self._conv_widgets[new_id])

    def update_widget(self, chat_id: int):
        button = QPushButton(str(self._db[self.chat_id].users))
        self.chat_buttons.addButton(button, self.chat_id)
        self._conv_widgets[self.chat_id] = button

    def load_chats(self):
        for chat in self._db:
            print(chat.id)
            button = QPushButton(str(chat.users))
            self.layout().addWidget(button)
            self.chat_buttons.addButton(button, chat.id)
            self._conv_widgets[chat.id] = button