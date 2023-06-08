import sys
from PySide2 import QtCore, QtGui, QtWidgets


class MyTab(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MyTab, self).__init__()
        self.parent = parent

        self.lineEdit = QtWidgets.QLineEdit('Введите номер из 4х цифр')

        self.pushButton = QtWidgets.QPushButton('Создать TableWidget')

        self.tableWidget = QtWidgets.QTableWidget(0, 4)
        self.tableWidget.setHorizontalHeaderLabels(['IP', 'Number', 'SSH', 'VNC'])
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)

        vbox = QtWidgets.QVBoxLayout(self)
        vbox.addWidget(self.tableWidget)
        vbox.addWidget(self.lineEdit)
        vbox.addWidget(self.pushButton)


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.centralwidget = QtWidgets.QWidget()
        self.setCentralWidget(self.centralwidget)

        # + vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
        self.tabWidget = QtWidgets.QTabWidget()
        count = self.tabWidget.count()
        self.nb = QtWidgets.QToolButton(text="Добавить", autoRaise=True)
        self.nb.clicked.connect(self.new_tab)
        self.tabWidget.insertTab(count, QtWidgets.QWidget(), "")
        self.tabWidget.tabBar().setTabButton(
            count, QtWidgets.QTabBar.RightSide, self.nb)

        self.new_tab()

        self.layout = QtWidgets.QGridLayout(self.centralwidget)
        self.layout.addWidget(self.tabWidget)



    def new_tab(self):
        index = self.tabWidget.count() - 1
        tabPage = MyTab(self)
        self.tabWidget.insertTab(index, tabPage, f"Tab {index}")
        self.tabWidget.setCurrentIndex(index)
        #tabPage.lineEdit.setFocus()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold))
    win = MyWindow()
    win.resize(640, 480)
    win.show()
    sys.exit(app.exec_())