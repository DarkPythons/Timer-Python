"""
Файл, который содержит основные функции для работы программы 
"""

import pandas as pd
from class_timer import TimerClass
import time

def create_new_timer(name_timer: str):
    # Делаем создание объекта таймера от класса таймера
    timer_object = TimerClass(name_timer)
    # Делаем помещение этого объекта таймера в общий словарь наших таймеров
    timers_dict = {name_timer : timer_object}
    return timers_dict

def get_timers_list(all_timers_dict: dict[str, TimerClass]):
    print("Список всех доступных таймеров: ")

    timers_object_list = all_timers_dict.values()

    timers_object_list = list(timers_object_list)

    # Если объектов таймера еще нет
    if not timers_object_list:
        print("У вас пока нет таймеров, обратитесь к команде create.")
        time.sleep(1)

    return timers_object_list

def prints_list_timers(timers_object_list: list):
    for object_timer in timers_object_list:
        # Делаем вывод объекта нашего таймерa, у него уже подготовлен метод __str__
        print(object_timer)
    
def get_name_number_task(timers_object_list: list, task_message: str):
    prints_list_timers(timers_object_list)

    name_or_number_timer = input(f"Введите название или номер вашего таймера для {task_message}: ")

    return name_or_number_timer

def get_lists_numbers_and_names_timers(timers_object_list: list, all_timers_dict: dict):
    list_number_timers: list = [str(timer_object.timer_object_count) for timer_object in timers_object_list]

    list_name_timers: list = all_timers_dict.keys() 

    return list_number_timers, list_name_timers

def get_list_numbers_timers(timers_object_list: list):
    list_numbers_timers = [timers_object.timer_object_count for timers_object in timers_object_list]
    return list_numbers_timers

def get_list_names_timers(timers_object_list: list):
    list_names_timers = [timers_object.name_timer for timers_object in timers_object_list]
    return list_names_timers


def create_lists_hour_min_sec(timers_object_list: list):
    list_hours_timers = []
    list_minutes_timers = []
    list_seconds_timers = []

    for timer_object in timers_object_list:
        # Делаем получение словаря времени, которое было на таймере
        dict_timers_time: dict[str, int] = timer_object.second_to_hour_min_sec()
        # Делаем распаршивание этого словаря по ключам
        hours: int = dict_timers_time["hours"]
        minutes: int = dict_timers_time["minutes"]
        seconds: int = dict_timers_time["seconds"]

        # Делаем добавление наших часов, минут и секунд в списки
        list_hours_timers.append(hours)
        list_minutes_timers.append(minutes)
        list_seconds_timers.append(seconds)

    tuple_times = (list_hours_timers, list_minutes_timers, list_seconds_timers,)
    return tuple_times

def configure_data_to_pandas(timers_object_list: list):

    list_numbers_timers: list[int, int] = get_list_numbers_timers(timers_object_list)
    list_name_timers: list[str, str] = get_list_names_timers(timers_object_list)

    
    # Делаем получение списка часов, минут и секунд на таймерах
    list_hours_timers, list_minutes_timers, list_seconds_timers = create_lists_hour_min_sec(timers_object_list)


    dict_data_pandas = {
        # Указываем как ключ название столбца, а как значение, список значений который будет в этом столбце
        "Номер таймера" : list_numbers_timers,
        "Название таймера" : list_name_timers,
        "Часы" : list_hours_timers,
        "Минуты" : list_minutes_timers,
        "Секунды" : list_seconds_timers
    }

    return dict_data_pandas

def view_data_in_pandas_table(data_to_pandas: dict[str, list]):
    # Создаем фрейм на основании наших данных
    data_frame = pd.DataFrame(data_to_pandas)
    # Выводим нашу таблицу данных
    print(data_frame)

def view_all_information_timers(timers_object_list: list):

    # Если в списке таймеров есть хотя бы один таймер
    if timers_object_list:
        # Делаем создание словаря, который пойдет в создание фрейма pandas, на основании данных из всех таймеров
        data_to_pandas: dict[str, list] = configure_data_to_pandas(timers_object_list)
        # Делаем вызов функции, которая выведет наши данные как таблица, передавая наши данные
        view_data_in_pandas_table(data_to_pandas)
