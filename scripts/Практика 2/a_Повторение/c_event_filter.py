"""
Файл для повторения темы фильтр событий

Напомнить про работу с фильтром событий.

Предлагается создать кликабельный QLabel с текстом "Красивая кнопка",
используя html - теги, покрасить разные части текста на нём в разные цвета
(красивая - красным, кнопка - синим)
"""

from PySide6 import QtWidgets, QtCore


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUi()
        self.initSignals()

    def initUi(self):

        self.LineEditInput = QtWidgets.QLineEdit()
        self.LineEditMirror = QtWidgets.QLineEdit()
        self.pushButtonMirror = QtWidgets.QPushButton("Отобрази")
        layout_h = QtWidgets.QHBoxLayout()
        layout_v = QtWidgets.QVBoxLayout()
        layout_h.addWidget(self.LineEditInput)
        layout_h.addWidget(self.LineEditMirror)

        layout_v.addLayout(layout_h)
        layout_v.addWidget(self.pushButtonMirror)

        self.setLayout(layout_v)

    def initSignals(self):
        # self.pushButtonMirror.connect(self.pushButtonMirror, "clicked", self.reverseData) # уход от кликедов не получилось

        self.pushButtonMirror.clicked.connect(self.reverseData)  # сигнал №1
        # self.pushButtonMirror.clicked.connect(self.reverseData2) #сигнал №2
        # self.LineEditInput.textChanged.connect(self.reverseData3) #сигнал №3
        # self.LineEditInput.textChanged.connect(lambda text: self.LineEditMirror.setText(text[::-1]))

    def reverseData(self):
        get_data = self.LineEditInput.text()
        rev = get_data[::-1]
        self.LineEditMirror.setText(rev)

    def reverseData2(self, data):
        self.LineEditMirror.setText(self.LineEditInput.text()[::-1])  # элегантное решение в одну строчку

    def reverseData3(self, text):
        self.LineEditMirror.setText(text[::-1])

    def eventFilter(self, watched: QtCore.QObject, event: QtCore.QEvent) -> bool: #переопределяем

        if watched == self.pushButtonMirror:
            if event.type() == QtCore.QEvent.Type.Enter:
                self.pushButtonMirror.setText("Вошли в поле действия")
            if event.type() == QtCore.QEvent.Type.Leave:
                self.pushButtonMirror.setText("Отобрази")

        if watched == self.label:
            if event.type() == QtCore.QEvent.Type.Wheel:
                self.label.setText("<span style=' color:#aa0000;'>Красивая </span><span style=' color:#0000ff;'>кнопка</span>")
            if event.type() == QtCore.QEvent.Type.Leave:
                self.label.setText("Красивая кнопка")


        return super().eventFilter(watched, event)

if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
