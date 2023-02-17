from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton


class DataEntry(QWidget):
    def __init__(self, label):
        super(DataEntry, self).__init__()
        self.setLayout(QVBoxLayout())
        self.label = QLabel(label)
        self.field = QLineEdit()
        self.layout().addWidget(self.label)
        self.layout().addWidget(self.field)

    def text(self):
        # using cpp style text() to be style compliant with other pyqt5 widgets
        return self.field.text()

    def clear(self):
        self.field.setText('')


class TextWithButton(QWidget):
    def __init__(self, button_text: str):
        super(TextWithButton, self).__init__()
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        self.button = QPushButton(button_text)
        self.text_field = QLineEdit()
        self.layout.addWidget(self.text_field)
        self.layout.addWidget(self.button)

    def text(self) -> str:
        return self.text_field.text()

    def clear(self) -> None:
        self.text_field.setText('')