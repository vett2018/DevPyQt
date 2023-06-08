from PySide2 import QtWidgets, QtCore, QtGui
from PySide2 import QtWebEngineWidgets

from widget2 import Ui_MainWindow  # Импортируем класс формы


class Window(QtWidgets.QMainWindow):  # наследуемся от того же класса, что и форма в QtDesigner
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.index = 3
        self.initUi()
        self.initSignals()



    def initUi(self):
        #self.button = QtWidgets.QPushButton("Добавить Вкладку")
        #self.ui.horizontalLayout.addWidget(self.button)
        print(self.ui.tab.children())
        self.tabs = {}
        #self.tabs["tab"] = {"tab": self.ui.tab, "lineEdit": self.ui.lineEdit, "PushButton": self.ui.pushButton, "Web": self.ui.webEngineView}
        self.tabs["tab"] = {"tab": self.ui.tab, "Web": self.ui.webEngineView}

        self.tabs["tab_2"] = {"tab": self.ui.tab, "other": []}



    def initSignals(self):
        self.ui.pushButton.clicked.connect(self.setUrl)
        #self.button.clicked.connect(self.createTab)
        self.ui.pushButton_2.clicked.connect(self.createTab)


    def newTab(self):
        # eval(f"self.tab_{index}=QtWidgets.QWidget()")
        tab = QtWidgets.QWidget()
        verticalLayout_2 = QtWidgets.QVBoxLayout(tab)
        horizontalLayout_2 = QtWidgets.QHBoxLayout()
        #lineEdit = QtWidgets.QLineEdit(tab)
        #horizontalLayout_2.addWidget(lineEdit)

        pushButton = QtWidgets.QPushButton(tab)
        icon = QtGui.QIcon()
        icon.addFile(u":/logo/icons8-\u0434\u0436\u0435\u0439\u043a-16.png", QtCore.QSize(), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        pushButton.setIcon(icon)

        horizontalLayout_2.addWidget(pushButton)

        verticalLayout_2.addLayout(horizontalLayout_2)

        webEngineView = QtWebEngineWidgets.QWebEngineView(tab)
        webEngineView.setUrl(QtCore.QUrl(u"about:blank"))

        verticalLayout_2.addWidget(webEngineView)
        #self.tabs[f"tab_{self.index}"] = {"tab": tab, "lineEdit": lineEdit, "pushButton": pushButton, "Web": webEngineView}
        self.tabs[f"tab_{self.index}"] = {"tab": tab, "pushButton": pushButton, "Web": webEngineView}

        self.index += 1
        return tab



    def createTab(self):
        #tab = self.newTab()
        # print(tab.children())
        self.ui.tabWidget.addTab(self.newTab(), "Новая Вкладка")
        tab = self.tabs[f"tab_{self.index - 1}"]
        #tab["pushButton"].clicked.connect(lambda: tab["Web"].setUrl("https://" + tab["lineEdit"].text())) # Old
        tab["pushButton"].clicked.connect(lambda: tab["Web"].setUrl("https://ya.ru"))


    def setUrl(self):
        # self.ui.webEngineView.setUrl("https://" + self.ui.lineEdit.text())
        self.ui.webEngineView.setUrl("https://ya.ru")


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec_()

