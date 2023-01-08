import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit, QPushButton, QLabel, QVBoxLayout, QWidget
from app.client.gui.chat import ChatBox






app = QApplication(sys.argv)


window = QMainWindow()
QMainWindow.setCentralWidget()
window.show()
app.exec()