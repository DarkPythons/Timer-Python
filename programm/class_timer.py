"""
Файл который содержит класс самого таймера.
"""
import time


class TimerClass(object):
    __count_of_timer = 0

    # Магический метод инициализации новых объектов от класса таймера
    def __init__(self, timer_name: str) -> None:
        self.name_timer = timer_name
        self.count_time = 0
        self.timer_object_count = self.__count_of_timer
        self.__add_count()

    @classmethod
    def __add_count(cls):
        cls.__count_of_timer += 1

    # Метод для того чтобы таймер запустился
    def start(self):
        print(f"Таймер '{self.name_timer}' был запущен.")

        start_timer_time = time.time()

        finished_answer = input("Введите любое значение для того, чтобы остановить таймер: \n")

        finished_timer_time = time.time()

        time_count = round(finished_timer_time - start_timer_time, 3)

        # Делаем перевод количества секунд в часы/минуты/секунды
        times_dict = self.second_to_hour_min_sec_static(time_count)

        print(f"За эту итерацию таймер '{self.name_timer}' насчитал: ")
        print(f"{times_dict["hours"]} часов")
        print(f"{times_dict["minutes"]} минут")
        print(f"{times_dict["seconds"]} секунд")

        # Делаем прибавление нашего получившегося значения которое было насчитано к общему таймеру
        self.count_time += time_count

        # Делаем вызов метода, который секунды у объекта таймера переведет в часы/минуты/секунды
        times_dict_general = self.second_to_hour_min_sec()

        print(f"Общее время на таймере за все итерации: ")
        print(f"{times_dict_general["hours"]} часов")
        print(f"{times_dict_general["minutes"]} минут")
        print(f"{times_dict_general["seconds"]} секунд")
        time.sleep(1)

    def restart(self):
        self.count_time = 0
        print(f"'{self.name_timer}' был сброшен на 0.")

    @staticmethod
    def second_to_hour_min_sec_static(time_in_second: int):
        """Метод для перевода пришедшего количества секунд в часы/минуты/секунды"""
        second_time = time_in_second % 60
        minutes_time = (time_in_second // 60) % 60
        hours_time = time_in_second // 3600

        times_dict = {
            "hours" : hours_time,
            "minutes" : minutes_time,
            "seconds" : second_time
        }
        return times_dict
    
    def print_information(self):
        """Метод для вывода всей информации, которая есть у таймера"""

        # Делаем перевод секунд, которыe есть у таймера в часы/минуты/секунды
        times_dict_timer = self.second_to_hour_min_sec()
        print()
        print(f"Номер таймера: {self.timer_object_count}")
        print(f"Название таймера: '{self.name_timer}'")
        print(f"Часы: {times_dict_timer['hours']}")
        print(f"Минуты: {times_dict_timer['minutes']}")
        print(f"Секунды: {times_dict_timer['seconds']}")


    def second_to_hour_min_sec(self):
        """Метод для перевода секунд на таймере в часы/минуты/секунды"""
        second_time = self.count_time % 60
        minutes_time = (self.count_time // 60) % 60
        hours_time = self.count_time // 3600

        times_dict = {
            "hours" : hours_time,
            "minutes" : minutes_time,
            "seconds" : second_time
        }

        return times_dict


    def __str__(self):
        return f"[{self.timer_object_count}] {self.name_timer}"
    
