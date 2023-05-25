"""
Модуль в котором содержаться потоки Qt
"""

import time
import psutil
import requests
import json

from PySide2 import QtCore


class SystemInfo(QtCore.QThread):
    systemInfoReceived = QtCore.Signal(list)  # TODO Создайте экземпляр класса Signal и передайте ему в конструктор тип данных передаваемого значения (в текущем случае list)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.delay = None  # TODO создайте атрибут класса self.delay = None, для управлением задержкой получения данных

    def run(self) -> None:  # TODO переопределить метод run
        if self.delay is None:  # TODO Если задержка не передана в поток перед его запуском
            self.delay = 1  # TODO то устанавливайте значение 1

        while True:  # TODO Запустите бесконечный цикл получения информации о системе
            cpu_value = psutil.cpu_percent()  # TODO с помощью вызова функции cpu_percent() в пакете psutil получите загрузку CPU
            ram_value = psutil.virtual_memory().percent  # TODO с помощью вызова функции virtual_memory().percent в пакете psutil получите загрузку RAM
            self.systemInfoReceived.emit([cpu_value, ram_value])  # TODO с помощью метода .emit передайте в виде списка данные о загрузке CPU и RAM
            time.sleep(self.delay)  # TODO с помощью функции .sleep() приостановите выполнение цикла на время self.delay


class WeatherHandler(QtCore.QThread):
    # TODO Пропишите сигналы, которые считаете нужными
    weatherReceived = QtCore.Signal(dict)

    def __init__(self, lat, lon, parent=None):
        super().__init__(parent)

        self.__api_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        self.__delay = 10
        self.__status = None

        @property
        def api_url(self) -> str:
            return self.__api_url

        @property
        def delay(self) -> int:
            return self.__delay

        @delay.setter
        def delay(self, value: int) -> None:
            if not isinstance(value, int):
                raise ValueError
            self.__delay = value

        @property
        def status(self) -> None:
            return self.__status

        @status.setter
        def status(self, value: bool) -> None:
            if not isinstance(value, bool):
                raise ValueError
            self.__status = value

    # def setDelay(self, delay) -> None:
    #     """
    #     Метод для установки времени задержки обновления сайта
    #
    #     :param delay: время задержки обновления информации о доступности сайта
    #     :return: None
    #     """
    #
    #     self.__delay = delay

    def run(self) -> None:
        # TODO настройте метод для корректной работы
        self.status = True

        while self.__status:
            response = requests.get(self.__api_url)
            if response.status_code == 200:
                data_dict = json.loads(response.json())
                self.weatherReceived.emit(data_dict["current_weather"])
                time.sleep(self.delay)
            else:
                self.status = False
                return
            # TODO Примерный код ниже
            """
            response = requests.get(self.__api_url)
            data = response.json()
            ваш_сигнал.emit(data)
            sleep(delay)
            """
