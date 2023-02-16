from PyQt5.QtWidgets import QVBoxLayout, QPushButton, QTextEdit, QButtonGroup, QWidget
from app.client.database.conversations import ConvDB


# temporary counter of conversation id, will be later replaced with request to server


class Conversations(QWidget):
    tmp_counter = 0

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
        self._db[self.tmp_counter] = [self.username_field.toPlainText()]
        self.username_field.setText('')
        self.update_widget(self.tmp_counter)
        self.layout().addWidget(self._conv_widgets[self.tmp_counter])
        self.tmp_counter += 1

    def update_widget(self, id: int):
        button = QPushButton(str(self._db[self.tmp_counter].users))
        self.chat_buttons.addButton(button, self.tmp_counter)
        self._conv_widgets[self.tmp_counter] = button

    def load_chats(self):
        print('fdsfds')
        for chat in self._db:
            print(chat.id)
            button = QPushButton(str(chat.users))
            self.layout().addWidget(button)
            self.chat_buttons.addButton(button, chat.id)
            self._conv_widgets[chat.id] = button