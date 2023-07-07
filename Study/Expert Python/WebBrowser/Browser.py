import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QLineEdit, QAction, QTabWidget, QMenu, QMenuBar


class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Krypton Web")
        self.setGeometry(100, 100, 800, 600)

        self.create_toolbar()
        self.create_searchbar()
        self.create_settings_menu()

        self.tabs = QTabWidget(self)
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)
        self.setCentralWidget(self.tabs)

        self.add_tab()

        self.show()

    def create_toolbar(self):
        self.toolbar = QToolBar()
        self.addToolBar(self.toolbar)

        back_button = QAction("<", self)
        # back_button.triggered.connect(self.view.back)
        self.toolbar.addAction(back_button)

        forward_button = QAction(">", self)
        # forward_button.triggered.connect(self.view.forward)
        self.toolbar.addAction(forward_button)

        refresh_button = QAction("+", self)
        refresh_button.triggered.connect(self.refresh)
        self.toolbar.addAction(refresh_button)

        add_tab_button = QAction("+ Tab", self)
        add_tab_button.triggered.connect(self.add_tab)
        self.toolbar.addAction(add_tab_button)

    def create_searchbar(self):
        self.search_bar = QLineEdit()
        self.search_bar.returnPressed.connect(self.load_url)
        self.toolbar.addWidget(self.search_bar)

    def create_settings_menu(self):
        settings_menu = self.menuBar().addMenu("Settings")

        white_action = settings_menu.addAction("White")
        white_action.triggered.connect(lambda: self.apply_theme("white"))

        grey_action = settings_menu.addAction("Grey")
        grey_action.triggered.connect(lambda: self.apply_theme("grey"))

        dark_action = settings_menu.addAction("Dark")
        dark_action.triggered.connect(lambda: self.apply_theme("dark"))

    def apply_theme(self, theme):
        if theme == "white":
            stylesheet = "background-color: white;"
        elif theme == "grey":
            stylesheet = "background-color: grey;"
        elif theme == "dark":
            stylesheet = "background-color: black; color: white;"
        else:
            return

        self.setStyleSheet(stylesheet)

    def load_url(self):
        url = self.search_bar.text()
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "http://" + url
        self.view.load(QUrl(url))

    def refresh(self):
        self.view.load(self.view.url())

    def add_tab(self):
        view = QWebEngineView()
        view.load(QUrl("https://www.google.com"))
        self.tabs.addTab(view, "New Tab")

    def close_tab(self, index):
        self.tabs.removeTab(index)


app = QApplication(sys.argv)
browser = Browser()
sys.exit(app.exec_())
