from PyQt5.QtWidgets import QVBoxLayout, QPushButton, QTextEdit
from app.client.database.conversations import ConvDB


# temporary counter of conversation id, will be later replaced with request to server


class Conversations(QVBoxLayout):
    tmp_counter = 0

    def __init__(self, conv_db: ConvDB = ConvDB()):
        super().__init__()
        self._db = conv_db
        self._conv_widgets = {}
        add_conv = QPushButton('Add conversation')
        add_conv.clicked.connect(self.new_conversation)
        self.username_field = QTextEdit()
        self.addWidget(add_conv)
        self.addWidget(self.username_field)

    def new_conversation(self):
        self._db[self.tmp_counter] = [self.username_field.toPlainText()]
        self.username_field.setText('')
        self.update_widget(self.tmp_counter)
        self.addWidget(self._conv_widgets[self.tmp_counter])
        self.tmp_counter += 1

    def update_widget(self, id: int):
        self._conv_widgets[self.tmp_counter] = QPushButton(str(self._db[self.tmp_counter].users))