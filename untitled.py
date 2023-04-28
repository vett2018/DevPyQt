# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDateTimeEdit,
    QDial, QDoubleSpinBox, QFontComboBox, QGraphicsView,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPlainTextEdit, QProgressBar, QSizePolicy, QSlider,
    QSpinBox, QStatusBar, QTextBrowser, QTextEdit,
    QTimeEdit, QWidget)

from tictactoe import TicTacToe
from wigglywidget import WigglyWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1008, 713)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(170, 50, 231, 81))
        self.fontComboBox = QFontComboBox(self.centralwidget)
        self.fontComboBox.setObjectName(u"fontComboBox")
        self.fontComboBox.setGeometry(QRect(630, 70, 210, 22))
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(130, 170, 113, 22))
        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(70, 250, 104, 71))
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(390, 220, 321, 101))
        self.spinBox = QSpinBox(self.centralwidget)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(760, 220, 291, 41))
        self.doubleSpinBox = QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setGeometry(QRect(680, 150, 231, 41))
        self.timeEdit = QTimeEdit(self.centralwidget)
        self.timeEdit.setObjectName(u"timeEdit")
        self.timeEdit.setGeometry(QRect(370, 360, 118, 22))
        self.dateEdit = QDateEdit(self.centralwidget)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(510, 360, 110, 22))
        self.dateTimeEdit = QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        self.dateTimeEdit.setGeometry(QRect(650, 360, 194, 22))
        self.dial = QDial(self.centralwidget)
        self.dial.setObjectName(u"dial")
        self.dial.setGeometry(QRect(810, 540, 141, 71))
        self.horizontalSlider = QSlider(self.centralwidget)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setGeometry(QRect(460, 70, 160, 22))
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.verticalSlider = QSlider(self.centralwidget)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setGeometry(QRect(210, 280, 22, 160))
        self.verticalSlider.setOrientation(Qt.Vertical)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(830, 490, 341, 51))
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(320, 470, 311, 71))
        self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(270, 200, 256, 192))
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(90, 590, 118, 23))
        self.progressBar.setValue(24)
        self.ticTacToe = TicTacToe(self.centralwidget)
        self.ticTacToe.setObjectName(u"ticTacToe")
        self.ticTacToe.setGeometry(QRect(90, 350, 200, 200))
        self.wigglyWidget = WigglyWidget(self.centralwidget)
        self.wigglyWidget.setObjectName(u"wigglyWidget")
        self.wigglyWidget.setGeometry(QRect(340, 290, 400, 200))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1008, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"New Item", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"New Item", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"New Item", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"New Item", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"New Item", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"New Item", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"New Item", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"New Item", None))
        self.comboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"New Item", None))
        self.comboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"New Item", None))
        self.comboBox.setItemText(10, QCoreApplication.translate("MainWindow", u"New Item", None))

        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"\u0440\u0440\u0440\u0440", None))
        self.plainTextEdit.setPlainText(QCoreApplication.translate("MainWindow", u"\u0432\u0440\u0432\u0440\u0440\u0432\u0440\u0430\u043e\u0430\u043e\u0430\u043e\u043e\u0430 ", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:48pt; font-weight:700; font-style:italic; text-decoration: underline;\">\u0432\u0440\u0432\u0440\u0432\u0440\u0440</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0412\u0412\u0412\u0412\u0412\u0412\u0412\u0412\u0412\u0412\u0412\u0412\u0412\u0412\u0412", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">\u043d\u043d\u043d\u043d\u043d\u043d\u043d\u043d\u043d\u043d</span></p></body></html>", None))
        self.ticTacToe.setProperty("state", QCoreApplication.translate("MainWindow", u"-X-XO----", None))
        self.wigglyWidget.setProperty("text", QCoreApplication.translate("MainWindow", u"Hello, world", None))
    # retranslateUi

