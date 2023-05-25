"""
Реализовать окно, которое будет объединять в себе сразу два предыдущих виджета
"""
from PySide2 import QtWidgets

from b_systeminfo_widget import SystemInfoWindow  # Импортируем класс формы
from c_weatherapi_widget import WeatherInfo


# class Window(QtWidgets.QMainWindow):  # наследуемся от того же класса, что и форма в QtDesigner
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         # self.centralwidget = QtWidgets.QWidget(self)
#         self.horizontalLayout = QtWidgets.QHBoxLayout()
#         self.app1 = SystemInfoWindow(self)
#         self.app2 = WeatherInfo(self)
#         self.horizontalLayout.addWidget(self.app1)
#         self.horizontalLayout.addWidget(self.app2)
#         # self.setCentralWidget(self.centralwidget)
#         self.setLayout(self.horizontalLayout)


class Window(QtWidgets.QWidget):  # наследуемся от того же класса, что и форма в QtDesigner
    def __init__(self, parent=None):
        super().__init__(parent)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.app1 = SystemInfoWindow()
        self.app2 = WeatherInfo()
        self.horizontalLayout.addWidget(self.app1)
        self.horizontalLayout.addWidget(self.app2)
        self.setLayout(self.horizontalLayout)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()