"""
Модуль, где находятся основные функции для сохранения диагрммы в файл
"""

import matplotlib.pyplot as plt

from timer.class_timer import Timer
from timer.function_timers import get_timers_list, get_list_names_timers, get_list_seconds_timers
from .utils import create_diagram_object



def save_diagram_to_file(file_path: str, dict_timers_all: dict[str, Timer]) -> None:
    """
    Функция для сохранения диаграммы, которая уже была выведена в файл
    file_path - путь до файла, куда нужно будет поместить диаграмму
    """
    # Делаем получение только объектов таймеров помещая эти объекты в список
    timers_object_list: list[Timer] = get_timers_list(dict_timers_all)
    # Получение всех названий таймеров
    timers_names_list: list[str, str] = get_list_names_timers(timers_object_list)
    # Получение списка секунд, которые насчитали все таймеры в виде списка
    timers_second_list: list[int, int] = get_list_seconds_timers(timers_object_list)

    # Создание объекта диаграммы
    diagram_object: plt = create_diagram_object(timers_second_list, timers_names_list)
    
    # Сохранение объекта диаграммы в файл по указанному пути
    diagram_object.savefig(file_path)