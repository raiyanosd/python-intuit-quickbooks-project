import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView

class MainWindow(QMainWindow):
def__init__(self, *args, **kwargs):
super(MainWindow, self).__init__(*args, **kwargs)

self.setWindowTitle("My Web Browser")
self.setGeometry(100, 100, 1280, 720)

self.browser = QWebEngineView()
self.setCentralWidget(self.browser)

def navigate_to_url(self):
url = self.url_bar.text()
self.browser.setUrl(QUrl(url))

navbar = QToolBar("Navigation")
self.addToolBar(navbar)

self.url_bar = QLineEdit()
self.url_bar.returnPressed.connect(self.navigate_to_url)
navbar.addWidget(self.url_bar)

back_button = QAction(QIcon("back.png"), "Back", self)
back_button.triggered.connect(self.browser.back)
navbar.addAction(back_button)

forward_button = QAction(QIcon("forward.png"), "Forward", self)
forward_button.triggered.connect(self.browser.forward)
navbar.addAction(forward_button)

if __name__ == '__main__':
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
