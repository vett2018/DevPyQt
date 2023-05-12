"""
Файл для повторения темы сигналов

Напомнить про работу с сигналами и изменением Ui.

Предлагается создать приложение, которое принимает в lineEditInput строку от пользователя,
и при нажатии на pushButtonMirror отображает в lineEditMirror введённую строку в обратном
порядке (задом наперед).
"""

from PySide2 import QtWidgets


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

        self.pushButtonMirror.clicked.connect(self.reverseData) #сигнал №1
        #self.pushButtonMirror.clicked.connect(self.reverseData2) #сигнал №2
        #self.LineEditInput.textChanged.connect(self.reverseData3) #сигнал №3
        #self.LineEditInput.textChanged.connect(lambda text: self.LineEditMirror.setText(text[::-1]))

    def reverseData(self, data):
        print(data)
        get_data = self.LineEditInput.text()
        rev = get_data[::-1]
        self.LineEditMirror.setText(rev)

    def reverseData2(self, data):
        self.LineEditMirror.setText(self.LineEditInput.text()[::-1]) #элегантное решение в одну строчку

    def reverseData3(self, text):
        self.LineEditMirror.setText(text[::-1])


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
