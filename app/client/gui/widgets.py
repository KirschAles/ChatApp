from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit


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