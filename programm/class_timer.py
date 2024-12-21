"""
Файл, который содержит класс самого таймера.
"""
import time

class Timer(object):
    # Количество таймеров
    __count_of_timer: int = 0
    
    def __init__(self, timer_name: str) -> None:
        """
        Метод инициализации новых объектов таймеров
        self - сам объект таймера
        timer_name - название таймера
        """
        self.name_timer: str = timer_name
        self.count_time: int = 0
        self.timer_object_count: int = self.__count_of_timer
        self.__add_count()

    @classmethod
    def __add_count(cls) -> None:
        """Метод для увеличения количества таймеров образованных от класса Timer"""
        cls.__count_of_timer += 1

    def start(self) -> None:
        """
        Метод, который делает запуск таймера
        self - сам объект таймера
        """
        print(f"Таймер '{self.name_timer}' был запущен.")
        start_timer_time: float = time.time()
        # Таймер будет считать время до тех пор, пока пользователь не сделает ввод
        finished_answer: str = input("Введите любое значение для того, чтобы остановить таймер: \n> ")
        finished_timer_time: float = time.time()
        # Высчитываем количество прошедшего времени
        time_count: float = round(finished_timer_time - start_timer_time, 3)

        # Делаем перевод количества секунд в часы/минуты/секунды
        times_dict: dict[str, int] = self.second_to_hour_min_sec_static(time_count)

        print()

        print(f"За эту итерацию таймер '{self.name_timer}' насчитал: ")
        print(f"{times_dict['hours']} часов")
        print(f"{times_dict['minutes']} минут")
        print(f"{times_dict['seconds']} секунд")

        # Делаем прибавление нашего получившегося времени которое было насчитано к общему таймеру
        self.count_time += time_count

        # Делаем вызов метода, который секунды у объекта таймера переведет в часы/минуты/секунды
        times_dict_general: dict[str, int] = self.second_to_hour_min_sec()

        print(f"Общее время на таймере за все итерации: ")
        print(f"{times_dict_general['hours']} часов")
        print(f"{times_dict_general['minutes']} минут")
        print(f"{times_dict_general['seconds']} секунд")
        time.sleep(1)

    def restart(self) -> None:
        """
        Метод для обнуления общего количества времени, которое было посчитано таймером
        self - сам объект таймера
        """
        # Ставим общее количество времени на таймере на ноль
        self.count_time: int = 0
        print(f"'{self.name_timer}' был сброшен на 0.")

    @staticmethod
    def second_to_hour_min_sec_static(time_in_second: int) -> dict[str, int]:
        """
        Метод для перевода пришедшего количества секунд в часы/минуты/секунды
        time_in_second - количество секунд
        >>> second_to_hour_min_sec_static(3661)
        times_dict = {
            "hours" : 1,
            "minutes" : 1,
            "seconds" : 1
        }
        """

        # Делаем перевод секунд в часы/минуты/секунды
        hours_time: int = time_in_second // 3600
        minutes_time: int = (time_in_second // 60) % 60
        second_time: int = time_in_second % 60

        times_dict = {
            "hours" : hours_time,
            "minutes" : minutes_time,
            "seconds" : second_time
        }
        return times_dict
    
    def print_information(self) -> None:
        """
        Метод для вывода всей информации, которая есть у таймера
        self - сам объект таймера
        """

        # Делаем перевод секунд, которыe есть у таймера в часы/минуты/секунды
        times_dict_timer: dict[str, int] = self.second_to_hour_min_sec()
        print()
        print(f"Номер таймера: {self.timer_object_count}")
        print(f"Название таймера: '{self.name_timer}'")
        print(f"Часы: {times_dict_timer['hours']}")
        print(f"Минуты: {times_dict_timer['minutes']}")
        print(f"Секунды: {times_dict_timer['seconds']}")


    def second_to_hour_min_sec(self) -> dict[str, int]:
        """
        Метод для перевода секунд на таймере в часы/минуты/секунды
        self - сам объект таймера, внутри которого по атрибуту count_time
        лежит количество секунд, которое насчитал таймер, их мы и переводим
        Возвращается словарь с количеством часов, минут и секунд которое лежало в таймере
        """
        # Делаем перевод секунд в часы/минуты/секунды
        hours_time: int = self.count_time // 3600
        minutes_time: int = (self.count_time // 60) % 60
        second_time: int = round(self.count_time % 60, 3)

        times_dict = {
            "hours" : hours_time,
            "minutes" : minutes_time,
            "seconds" : second_time
        }
        return times_dict


    def __str__(self) -> str:
        """Метод для красивого и информационного вывода объектов таймера"""
        return f"[{self.timer_object_count}] {self.name_timer}"
    
