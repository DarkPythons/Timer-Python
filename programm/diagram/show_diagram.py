"""
Основные функции для вывода диаграммы на экран.
show_diagram - выводит диаграмму пользователю на экран, на основании данных таймеров 
"""

import matplotlib.pyplot as plt

from timer.class_timer import Timer
from timer.function_timers import get_timers_list, get_list_names_timers, get_list_seconds_timers
from .utils import create_diagram_object

def show_diagram(dict_timers_all: dict[str, Timer]) -> None:
    """
    Функция для подготовки данных и конечного вывода диаграммы
    dict_timers_all - словарь всех таймеров, где ключ это название таймера, 
    а значение - объект таймера
    """
    # Делаем получение только объектов таймеров помещая эти объекты в список
    timers_object_list: list[Timer] = get_timers_list(dict_timers_all)
    # Получение всех названий таймеров
    timers_names_list: list[str, str] = get_list_names_timers(timers_object_list)
    # Получение списка секунд, которые насчитали все таймеры в виде списка
    timers_second_list: list[int, int] = get_list_seconds_timers(timers_object_list)

    diagram_object: plt = create_diagram_object(timers_second_list, timers_names_list)
    # Делаем показ круговой диаграммы на экран
    diagram_object.show()