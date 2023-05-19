import sys  # sys нужен для передачи argv в QApplication
# from PySide2 import QtWidgets
# import c_signals_events  # Это наш конвертированный файл дизайна
#
# #PySide2-uic test_ui.ui -o test_ui.py - конвертация
#
#
# class ExampleApp(QtWidgets.QMainWindow):
#     def __init__(self):
#         # Это здесь нужно для доступа к переменным, методам
#         # и т.д. в файле design.py
#         super().__init__()
#         self.ui = c_signals_events.Ui_Form()
#         self.ui.setupUi(self)  # Это нужно для инициализации нашего дизайна
#
# def main():
#     app = QtWidgets.QApplication()  # Новый экземпляр QApplication
#     window = ExampleApp()  # Создаём объект класса ExampleApp
#     window.show()  # Показываем окно
#     app.exec_()  # и запускаем приложение
#
# if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
#     main()  # то запускаем функцию main()


from PySide6 import QtWidgets

from c_signals_events import *   # Импортируем класс формы


class Window(QtWidgets.QMainWindow):  # наследуемся от того же класса, что и форма в QtDesigner
    def __init__(self, parent=None):
        super().__init__(parent)

        # Создание "прокси" переменной для работы с формой
        self.ui = Ui_Form()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()


    app.exec_()
#
# # Ошибка return original_import(name, *args, **kwargs)
# # Ошибка ModuleNotFoundError: No module named 'ui'
