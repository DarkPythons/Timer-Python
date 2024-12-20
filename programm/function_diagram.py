"""
Модуль, который содержит основные функции для работы с диаграммой
"""

import matplotlib.pyplot as plt
from class_timer import TimerClass
from function_timers import get_timers_list, get_list_names_timers, get_list_seconds_timers

def diagram_pie_show(timers_second_list: list[int, int], timers_names_list: list[str, str]):
    """
    Функция для вывода диаграммы на экран с уже заготовленными данными:
    timers_second_list - список секунд, которые были насчитаны таймерами в отдельности
    timers_names_list - список названий таймеров
    """

    # Задаем название диаграммы
    plt.title("Соотношение времени и определенных задач.")
    # Создаем объект круговой диаграммы
    plt.pie(x=timers_second_list, labels=timers_names_list, autopct="%1.1f%%", startangle=180)
    # У круговой диаграммы включаем разделение по частям как у пирога
    plt.axis("equal")
    # Делаем вывод круговой диаграммы
    plt.show()

def show_diagram(dict_timers_all: dict[str, TimerClass]) -> None:
    """
    Функция для подготовки данных и конечного вывода диаграммы
    dict_timers_all - словарь всех таймеров, где ключ это название таймера, 
    а значение - объект таймера
    """
    # Делаем получение только объектов таймеров помещая эти объекты в список
    timers_object_list: list[TimerClass] = get_timers_list(dict_timers_all)
    # Получение всех названий таймеров
    timers_names_list: list[str, str] = get_list_names_timers(timers_object_list)
    # Получение списка секунд, которые насчитали все таймеры в виде списка
    timers_second_list: list[int, int] = get_list_seconds_timers(timers_object_list)

    diagram_pie_show(timers_second_list, timers_names_list)