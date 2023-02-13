from PyQt5.QtWidgets import QVBoxLayout, QLabel


class Conversations(QVBoxLayout):
    def __init__(self):
        super().__init__()
        title = QLabel("My Conversations")
        self.addWidget(title)
        self.addStretch()


