import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui, QtSvgWidgets

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.hello = ['"Making Hack Club, founder of it!" - some nice dude.', 'Hello World', "It's PHANTOM", ]

        self.button = QtWidgets.QPushButton("Don't Click Me")
        self.text = QtWidgets.QLabel(random.choice(self.hello), alignment=QtCore.Qt.AlignCenter)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

        ####Top-bar####
        
        self.top_bar = QtWidgets.QFrame()
        self.top_bar.setFixedHeight(100)

        self.layout.addWidget(self.top_bar)
        
        top_layout = QtWidgets.QHBoxLayout(self.top_bar)
        top_layout.setContentsMargins(15, 5, 15, 5)

        self.logo = QtSvgWidgets.QSvgWidget("flag-orpheus-top.svg")
        self.logo.setFixedSize(100, 100)

        top_layout.addWidget(self.logo)
        top_layout.addStretch()

    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))


   


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
