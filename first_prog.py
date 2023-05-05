from PySide6 import QtWidgets  # Импорт пакета, который содержит виджеты (окна, кнопки, и др.)

import sys
app = QtWidgets.QApplication(sys.argv) #создает объект программы на основе класса QApplication. Конструктор этого класса
                                       #принимает список параметров, переданных в командной строке

window = QtWidgets.QWidget() #создает объект окна в виде объекта класса QWidget. Этот класс наследуют практически
                             #все классы, реализующие компоненты графического интерфейс

window.setWindowTitle("Пepвaя программа на PyQt")
window.resize(300, 150)
label = QtWidgets.QLabel("<center><strong>!!! ВСЕМ ЗДРАВСТВУЙТЕ !!!</strong></center>")
btnQuit = QtWidgets.QPushButton("&ЗАКРЫТЬ ОКНО ")

vbox = QtWidgets.QVBoxLayout() #СОЗДАЕТ ВЕРТИКАЛЬНЫЙ КОНТЕЙНЕР
vbox.addWidget(label) #ДОБАВЛЕНИЕ НАДПИСИ В КОНТЕЙНЕР
vbox.addWidget(btnQuit) #дОБАВЛЕНИЕ КНОПКИ В КОНТЕЙНЕР

window.setLayout(vbox) # помещает контейнер в окно с помощью метода setLayout(). В результате контейнер
                        #станет потомком окна (а окно - родигелем контейнера).

btnQuit.clicked.connect(app.quit) #назначает обработчик сигнала clicked() кнопки,

window.show()
# sys.exit(app.exec())
app.exec_()  # Забуск бесконечного цикла приложения (событий)

