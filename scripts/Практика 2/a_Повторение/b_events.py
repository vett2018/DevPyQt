"""
Файл для повторения темы событий

Напомнить про работу с событиями.

Предлагается создать приложение, которое будет показывать все события происходящие в приложении,
(переопределить метод event), вывод событий производить в консоль.
При выводе события указывать время, когда произошло событие.
"""

from PySide6 import QtWidgets, QtCore, QtGui
import time


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

    def closeEvent(self, event: QtGui.QCloseEvent) -> None: #переопределение событий закрытие
        print("Close WINDOW")

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None: #переопределений событий с клавиатуры
        print(time.ctime(), event)  # перхват событий
        print(event.text())
        if event.text() == "H":
            print("HELLO")
            #self.destroy()
        return super().keyPressEvent(event) #что за строчка

    # def event(self, event: QtCore.QEvent) -> bool: #переопределить событие
    #     print(time.ctime(), event) #перхват событий
    #     #return super().event(event) #что за строчка


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
