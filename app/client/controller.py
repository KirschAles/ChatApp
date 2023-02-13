import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit, QPushButton, QLabel, QVBoxLayout, QWidget
from app.client.gui.conversations import Conversations





app = QApplication(sys.argv)

window = QMainWindow()
w = QWidget()
window.setCentralWidget(w)

w.setLayout(Conversations())
window.show()
app.exec()