import os
import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui, QtSvgWidgets, QtNetwork
from PySide6.QtNetwork import QNetworkAccessManager, QNetworkRequest
from PySide6.QtWebEngineWidgets import QWebEngineView
import json



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

        self.scroll = QtWidgets.QScrollArea()
        self.scroll.setWidgetResizable(True)

        self.scroll.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )

        self.scroll.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded
        )

        self.feed = QtWidgets.QWidget()
        self.feed_layout = QtWidgets.QVBoxLayout(self.feed)
        self.feed_layout.setContentsMargins(0,0,0,0)
        self.feed_layout.setSpacing(0)

        self.scroll.setWidget(self.feed)
        self.layout.addWidget(self.scroll)
        #body

    def fetch_short_videos(self):
        self.network_manager = QNetworkAccessManager(self)
        self.network_manager.finished.connect(self.on_video_fetched)

        api_url = QtCore.QUrl(
            "https://www.googleapis.com/youtube/v3/search?"
            "part=snippet"
            "&type=video"
            "&q=Hack+Club+Shorts"
            "&maxResults=10"
            "&key=nahuh"

        )    

        request = QNetworkRequest(api_url)
        self.network_manager.get(request)

    def on_video_fetched(self, reply):
        if reply.error() != QtNetwork.QNetworkReply.NetworkError.NoError:
            print("Error:", reply.errorString())
            reply.deleteLater()
            return

        data = json.loads(reply.readAll().data().decode("utf-8"))

        for item in data.get("items", []):
            video_id = item["id"].get("videoId")

            if video_id:
                title = item["snippet"]["title"]
                print("TITLE:", title)
                print("Video ID:", video_id)
                print("------------------")

                self.show_video(video_id)

        reply.deleteLater()


    def show_video(self, video_id):
        video = QWebEngineView()

        video.setUrl(
            QtCore.QUrl(
                f"https://www.youtube.com/shorts/{video_id}"
            )
        )

        video.setMinimumHeight(600)


        self.feed_layout.addWidget(video)

    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))


   


if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(
        QtCore.Qt.ApplicationAttribute.AA_UseSoftwareOpenGL
    )

    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(463, 692)
    widget.show()
    widget.fetch_short_videos()
    sys.exit(app.exec())
