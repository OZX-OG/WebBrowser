try:
    from PyQt5.QtWidgets import *
    from PyQt5.QtCore import *
    from PyQt5.QtGui import *
except:
    print("You need To Download Qt5 (pip install PyQt5)")

try:
    from PyQt5.QtWebEngineWidgets import *
except:
    print("You need To Download QtWebEngine (pip install PyQtWebEngine)")

try:
    from win32api import GetSystemMetrics
except:
    print("You need To Download win32 (pip install pywin32)")

from os import name, system

class MyWebBrowser():
    def __init__(self):
        
        self.window = QWidget()
        self.window.setWindowTitle("OZX-OG Web Browser")
        self.window.setGeometry(0, (GetSystemMetrics(0) / 2) - 500, GetSystemMetrics(0), 750)

        if name == 'nt':system('cls')
        else: system("clear")

        self.layout = QVBoxLayout()
        self.horizontal = QHBoxLayout()
        
        self.horizontal = QHBoxLayout()
        self.horizontal = QHBoxLayout()

        self.url_bar = QLineEdit()
        self.url_bar.setMaximumHeight(30)
        self.url_bar.setFont(QFont("senserif", 10))

        self.refresh = QPushButton("refresh")
        self.refresh.setMaximumHeight(30)
        self.refresh.setMaximumWidth(70)

        self.go_btn = QPushButton("search")
        self.go_btn.setMinimumHeight(30)

        self.back_btn = QPushButton("<")
        self.back_btn.setMinimumHeight(30)

        self.forward_btn = QPushButton(">")
        self.forward_btn.setMinimumHeight(30)

        self.horizontal.addWidget(self.url_bar)
        self.horizontal.addWidget(self.go_btn)
        self.horizontal.addWidget(self.back_btn)
        self.horizontal.addWidget(self.refresh)
        self.horizontal.addWidget(self.forward_btn)

        self.browser = QWebEngineView()

        self.url_bar.returnPressed.connect(lambda: self.navigate(self.url_bar.text()))
        self.go_btn.clicked.connect(lambda: self.navigate(self.url_bar.text()))
        self.back_btn.clicked.connect(self.browser.back)
        self.forward_btn.clicked.connect(self.browser.forward)
        self.refresh.clicked.connect(self.browser.reload)
        

        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)

        self.browser.setUrl(QUrl("https://google.com"))

        self.window.setLayout(self.layout)
        self.window.show()



    def navigate(self, url):
        if self.url_bar.text() == "" or self.url_bar.text() == "http://.com":
            url = "https://youtube.com"
            self.url_bar.setText(url)

        if not url.startswith("http"):
            url = "http://" + url
            self.url_bar.setText(url)
            
        self.browser.setUrl(QUrl(url))

app = QApplication([])
window = MyWebBrowser ()
if name == 'nt':system('cls')
else: system("clear")
app.exec_()
