"""
Файл для повторения темы QThread

Напомнить про работу с QThread.

Предлагается создать небольшое приложение, которое будет с помощью модуля request
получать доступность того или иного сайта (возвращать из потока status_code сайта).

Поработать с сигналами, которые возникают при запуске/остановке потока,
передать данные в поток (в данном случае url),
получить данные из потока (статус код сайта),
попробовать управлять потоком (запуск, остановка).

Опционально поработать с валидацией url
"""

from PySide6 import QtWidgets, QtCore
import requests
import time

class CheckSiteTread(QtCore.QThread):
    started_signal = QtCore.Signal()
    finished_signal = QtCore.Signal()
    status_code_signal = QtCore.Signal(int) #получить данные из сигнала
    result = QtCore.Signal(str)

    def __init__(self, parent=None, url="", sleep=3):
        super().__init__(parent)
        self.url = url
        self.sleep_ = sleep

    def run(self) -> None:
        #порабоать с сигналами потока чтобы отправить сигналы потока
        self.started_signal.emit()
        try:

            response = requests.get(self.url) # стучимся до сайта
            ststus_code = response.status_code
        except requests.exceptions.RequestException:
            ststus_code = None

        for val in range(10):
            self.result.emit(str(val))
            time.sleep(0.5)

        self.status_code_signal.emit(ststus_code)
        self.sleep(self.sleep_)
        self.finished_signal.emit()

class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUi()
        self.initThreads()
        self.initSignals()

    def initUi(self):
        self.urlLineEdit = QtWidgets.QLineEdit()
        self.checkButton = QtWidgets.QPushButton("Проверить")
        self.statusLabel = QtWidgets.QLabel()
        self.textEdit = QtWidgets.QPlainTextEdit()
        self.buttonQ =QtWidgets.QPushButton("Закончить Расчет")

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(QtWidgets.QLabel("URL"))
        layout.addWidget(self.urlLineEdit)
        layout.addWidget(self.textEdit)
        layout.addWidget(self.checkButton)
        layout.addWidget(self.buttonQ)
        layout.addWidget(self.statusLabel)

        self.setLayout(layout)

    def initThreads(self):
        self.threadSite = CheckSiteTread(sleep=3)
        self.threadSite.started_signal.connect(self.onTreadStart) #что будет происходит. сигнал из потока
        self.threadSite.finished_signal.connect(self.onTreadFinish)
        self.threadSite.status_code_signal.connect(self.onTreadStatus) #статус код
        self.threadSite.result.connect(self.textEdit.appendPlainText)


    def initSignals(self):
        self.checkButton.clicked.connect(self.onClick)
        #self.buttonQ.clicked.connect(self.threadSite.deleteLater)

    def onTreadStart(self):
        self.checkButton.setEnabled(False)
        self.textEdit.appendPlainText("Начали расчёт")

    def onTreadFinish(self):
        self.checkButton.setEnabled(True)
        self.textEdit.appendPlainText("Закончили расчёт")

    def onTreadStatus(self, value):
        if value is None:
            self.statusLabel.setText("Сайт не доступен")
        elif value == 200:
            self.statusLabel.setText("Сайт доступен")
        else:
            self.statusLabel.setText(f"Что-то не так код {value}")

    def onClick(self):
        url = self.urlLineEdit.text()
        self.threadSite.url = url
        self.threadSite.start()



if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
