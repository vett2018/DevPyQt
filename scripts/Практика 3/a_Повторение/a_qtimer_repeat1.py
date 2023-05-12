"""
Файл для повторения темы QTimer

Напомнить про работу с QTimer.

Предлагается создать приложение-которое будет
с некоторой периодичностью вызывать определённую функцию.
"""

from PySide6 import QtWidgets, QtCore
import time as time_


class Worker(QtCore.QThread):
    progress = QtCore.Signal(int)

    def __init__(self, func=None):
        self.func = func

    def run(self) -> None:
        """
        Метод имитирующий долгую задачу

        :return: None
        """
        if self.func is not None:
            self.func()
        self.finished.emit()


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()
        self.initTimers()
        self.initThreads()
        self.initSignals()

    def initUi(self) -> None:
        """
        Инициализация Ui

        :return: None
        """

        self.labelTime = QtWidgets.QLabel()
        self.labelTime.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.spinbox = QtWidgets.QSpinBox()
        self.plainText = QtWidgets.QPlainTextEdit()

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.labelTime)
        layout.addWidget(self.spinbox)
        layout.addWidget(self.plainText)

        self.setLayout(layout)

        self.showTime()

    def initTimers(self) -> None:
        """
        Инициализация таймеров

        :return: None
        """
        self.count = 0
        self.timeTimer = QtCore.QTimer()
        self.timeTimer.setInterval(1000)
        self.timeTimer.start()


    def initThreads(self) -> None:
        """
        Инициализация потоков

        :return: None
        """

        self.worker = Worker(self.showTime)


    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """

        self.timeTimer.timeout.connect(self.worker.start)
        self.timeTimer.timeout.connect(self.setText)
        self.spinbox.valueChanged.connect(self.setTimer)

    def showTime(self) -> None:
        """
        Слот для отображения в labelTime текущего времени

        :return: None
        """

        time = QtCore.QDateTime.currentDateTime()
        timeDisplay = time.toString('yyyy-MM-dd hh:mm:ss dddd')
        self.labelTime.setText(timeDisplay)
        time_.sleep(1)

    def setTimer(self, value):
        self.timeTimer.stop()
        self.timeTimer.setInterval(value * 1000 + 50)
        self.timeTimer.start()


    def setText(self):
        self.plainText.appendPlainText(str(self.count))
        self.count += 1



if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()