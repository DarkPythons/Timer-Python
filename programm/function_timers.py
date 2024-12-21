"""
Файл, который содержит основные функции для работы программы
"""

import pandas as pd
import time
from _collections_abc import dict_values

from class_timer import TimerClass

def create_new_timer(name_timer: str) -> dict[str, TimerClass]:
    """
    Функция для создания объекта таймера от класса таймера, принимает лишь название самого таймера
    name_timer - название таймера
    Делает возврат словаря, где как ключ лежит название таймера, а как значение объект таймера
    """
    # Делаем создание объекта таймера от класса таймера
    timer_object: TimerClass = TimerClass(name_timer)
    # Делаем помещение этого объекта таймера в общий словарь наших таймеров
    timers_dict: dict[str, TimerClass] = {name_timer : timer_object}
    return timers_dict

def get_timers_list(all_timers_dict: dict[str, TimerClass]) -> list[TimerClass]:
    """
    Функция для создания списка из объектов таймеров, принимает словарь, 
    где лежат как значения наши объекты, после чего создает список из этих значений
    """
    timers_object_list_values: dict_values[TimerClass] = all_timers_dict.values()
    timers_object_list: list[TimerClass, TimerClass] = list(timers_object_list_values)

    # Если объектов таймера еще нет
    if not timers_object_list:
        print("У вас пока нет таймеров, обратитесь к команде create.")
        time.sleep(1)

    return timers_object_list

def prints_list_timers(timers_object_list: list[TimerClass, TimerClass]) -> None:
    """
    Функция для перебора списка таймеров и их вывода при помощи цикла for, принимает
    сам список таймеров 
    """
    for object_timer in timers_object_list:
        # Делаем вывод объекта нашего таймерa, у него уже подготовлен метод __str__
        print(object_timer)
    
def get_name_number_task(timers_object_list: list[TimerClass], task_message: str):
    """
    Функция, где пользователю будет выведен список всех таймеров, и нужно будет ввести
    номер таймера или название таймера
    timers_object_list - список всех таймеров для их вывода
    task_message - указываем для какого действия будет вызван ввод названия или номера
    """
    # Вывод списка всех таймеров которые есть
    prints_list_timers(timers_object_list)
    name_or_number_timer = input(f"Введите название или номер вашего таймера для {task_message}: ")
    return name_or_number_timer

def get_list_numbers_timers(timers_object_list: list[TimerClass]) -> list[int, int]:
    """
    Функция для получения списка номеров всех таймеров
    timers_object_list - список из наших объектов таймеров, 
    из которого мы будем получать номера таймеров
    Возвращает список целых чисел, то есть наших номеров
    """
    list_numbers_timers = [timers_object.timer_object_count for timers_object in timers_object_list]
    return list_numbers_timers

def get_list_names_timers(timers_object_list: list[TimerClass]) -> list[str, str]:
    """
    Функция для получения списка названий всех таймеров
    timers_object_list - список из наших объектов таймеров, из которого мы будем получать названия таймеров
    Возвращает список строк, то есть наших названий таймеров
    """
    list_names_timers = [timers_object.name_timer for timers_object in timers_object_list]
    return list_names_timers

def get_lists_numbers_and_names_timers(
        timers_object_list: list[TimerClass]
    ) -> tuple[list[str, str], list[str, str]]:
    """
    Функция для получения списка всех номеров и названий у всех таймеров которые есть прямо сейчас
    timers_object_list - список наших таймеров
    all_timers_dict - словарь таймеров, где как ключи лежат названия таймеров, 
    как значения объекты таймеров
    """
    # Делаем получение всех номеров таймеров
    list_number_timers: list[int, int] = get_list_numbers_timers(timers_object_list)
    # Делаем превращение целых чисел в строки
    list_number_timers: list[str, str] = [str(one_num) for one_num in list_number_timers]

    # Делаем получение всех названий таймеров в виде списка
    list_name_timers: list[str, str] = get_list_names_timers(timers_object_list)
    return list_number_timers, list_name_timers


def create_lists_hour_min_sec(timers_object_list: list[TimerClass]) -> tuple[list[int|float]]:
    """
    Функция для создания списков часов, минут и секунд, которые будут использоваться как значения
    столбцов при выводе информации обо всех таймерах
    timers_object_list - список всех объектов таймеров
    Возвращает кортеж из списков
    """
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

    tuple_times: tuple[list] = (list_hours_timers, list_minutes_timers, list_seconds_timers,)
    return tuple_times



def configure_data_to_pandas(timers_object_list: list[TimerClass]) -> dict[str, list]:
    """
    Функция для конфигурирования данных для pandas, чтобы мы могли выводить таблицы инфорамции
    timers_object_list - список всех объектов таймеров 
    Возвращает словарь информации, где как ключи используются названия столбцов, 
    а как значения списки значений в этом столбце
    """

    list_numbers_timers: list[int, int] = get_list_numbers_timers(timers_object_list)
    list_name_timers: list[str, str] = get_list_names_timers(timers_object_list)
    
    # Делаем получение кортежа информации обо времени
    tuple_times: tuple[list, list, list] = create_lists_hour_min_sec(timers_object_list)

    # Делаем получение списка часов, минут и секунд на таймерах
    list_hours_timers, list_minutes_timers, list_seconds_timers = tuple_times

    dict_data_pandas: dict[str, list] = {
        # Указываем как ключ название столбца, а как значение, список значений который будет в этом столбце
        "Номер таймера" : list_numbers_timers,
        "Название таймера" : list_name_timers,
        "Часы" : list_hours_timers,
        "Минуты" : list_minutes_timers,
        "Секунды" : list_seconds_timers
    }

    return dict_data_pandas

def view_data_in_pandas_table(data_to_pandas: dict[str, list]) -> None:
    """
    Функция для вывода информации в виде таблицы pandas
    data_to_pandas - словарь информации, которую нужно вывести как таблица
    """
    # Создаем фрейм на основании наших данных
    data_frame: pd.DataFrame = pd.DataFrame(data_to_pandas)
    # Выводим нашу таблицу данных
    print(data_frame)


def view_all_information_timers(timers_object_list: list[TimerClass]) -> None:
    """
    Функция для вывода всей информации по всем таймерам в виде таблицы
    timers_object_list - список всех объектов таймеров, информацию из которого мы будем получать
    Функция ничего не возвращает, она лишь выводит информацию
    """

    # Если в списке таймеров есть хотя бы один таймер
    if timers_object_list:
        # Делаем создание словаря, который пойдет в создание фрейма pandas, на основании данных из всех таймеров
        data_to_pandas: dict[str, list] = configure_data_to_pandas(timers_object_list)
        # Делаем вызов функции, которая выведет наши данные как таблица, передавая наши данные
        view_data_in_pandas_table(data_to_pandas)

def get_timer_by_number(timers_object_list: list[TimerClass], number: int) -> TimerClass:
    """
    Функция для получения конкретного объекта таймера по его номеру
    timers_object_list - список всех объектов таймеров
    number - номер нашего таймера, по которому мы хотим вернуть объект таймера
    Возвращается объект таймера
    """

    # Получаем список номеров всех таймеров
    list_numbers_timers: list[int, int] = get_list_numbers_timers(timers_object_list)
    # Делаем поиск нашего номера в списке номеров таймеров
    index_object_timer: int = list_numbers_timers.index(number)

    # Получение нужного объекта таймера по его индексу
    timer_object: TimerClass = timers_object_list[index_object_timer]
    return timer_object

def get_list_seconds_timers(timers_object_list: list[TimerClass]) -> list[int, int]:
    """
    Функция для формирования списка секунд, которые были насчитаны каждым таймером в отдельности
    timers_object_list - список всех объектов таймеров
    """

    seconds_list: list[int, int] = [timer_object.count_time for timer_object in timers_object_list]
    return seconds_list

