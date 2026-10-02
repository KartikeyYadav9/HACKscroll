import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui, QtSvgWidgets
from PySide6.QtNetwork import QNetworkAccessManager, QNetworkRequest
from PySide6.QtWebEngineWidgets import QWebEngineView


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        #font

        font_id = QtGui.QFontDatabase.addApplicationFont("ShareTechMono-Regular.ttf")

        if font_id == -1:
            print("Font failed to load")
        else:
            font_family = QtGui.QFontDatabase.applicationFontFamilies(font_id)[0]
            app.setFont(QtGui.QFont(font_family))
       

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
        top_layout.setContentsMargins(10,0,0,0)
        top_layout.setSpacing(10)

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
            font-size: 54px;
            font-weight: bold;
            }
""")
        top_layout.addWidget(self.title)
        top_layout.addStretch()
        #body

        self.hello = ['"Making Hack Club, founder of it!" - some nice dude.', 'Hello World', "It's PHANTOM", ]

        self.button = QtWidgets.QPushButton("Don't Click Me")
        self.text = QtWidgets.QLabel(random.choice(self.hello), alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
        
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

    def fetch_short_videos(self):
        self.network_manager = QNetworkAccessManager(self)
        self.network_manager.finished.connect(self.on_videos_fetched)

        api_url = QtCore.QUrl(
            "https://www.googleapis.com/youtube/v3/search?"
            "part=snippet&type=video&videoDuration=short&q=coding+shorts&key=YOUR_API_KEY"
        )
    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))


   


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(463, 692)
    widget.show()

    sys.exit(app.exec())
