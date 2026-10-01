import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui, QtSvgWidgets

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        #font

        font_id = QtGui.QFontDatabase.addApplicationFont("ShareTechMono-Regular.ttf")

        if font_id == -1:
            print("Font failed to load")
        else:
            print(QtGui.QFontDatabase.applicationFontFamilies(font_id))

        app.setFont(QtGui.QFont("ShareTechMono-Regular.ttf"))

        ####Top-bar####
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.setContentsMargins(0,0,0,0)
        self.layout.setSpacing(0)
        self.top_bar = QtWidgets.QFrame()
        self.top_bar.setFixedHeight(110)

        self.top_bar.setStyleSheet("""
            QFrame {
            background-color: #338eda;
            border-bottom: 1px solid #111111;
            }
""")
        
        self.layout.addWidget(self.top_bar)
        
        top_layout = QtWidgets.QHBoxLayout(self.top_bar)
        top_layout.setContentsMargins(0,0,0,0)
        top_layout.setSpacing(0)

        self.logo = QtSvgWidgets.QSvgWidget("flag-orpheus-top.svg")
        self.logo.setFixedSize(50, 35)

        top_layout.addWidget(
            self.logo,
            0,
            QtCore.Qt.AlignmentFlag.AlignLeft |
            QtCore.Qt.AlignmentFlag.AlignTop
        )

        

        #header
        self.title = QtWidgets.QLabel("HACKscroll")

        self.title.setStyleSheet("""
            QLabel {
            color : white;
            font-size: 24px;
            font-weight: bold;
            border-bottom: 0px;
            }
""")
        top_layout.addWidget(
            self.title,
            0,
            QtCore.Qt.AlignmentFlag.AlignLeft |
            QtCore.Qt.AlignmentFlag.AlignVCenter
        )

        #body

        self.hello = ['"Making Hack Club, founder of it!" - some nice dude.', 'Hello World', "It's PHANTOM", ]

        self.button = QtWidgets.QPushButton("Don't Click Me")
        self.text = QtWidgets.QLabel(random.choice(self.hello), alignment=QtCore.Qt.AlignCenter)
        
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

        

    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))


   


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(463, 692)
    widget.show()

    sys.exit(app.exec())
