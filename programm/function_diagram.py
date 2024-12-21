"""
Модуль, который содержит основные функции для работы с диаграммой
"""

import matplotlib.pyplot as plt
import pandas as pd
from class_timer import TimerClass
from function_timers import get_timers_list, get_list_names_timers, get_list_seconds_timers

def create_pandas_object(data_to_pandas: dict[str, list]) -> pd.DataFrame:
    """
    Функция для перевода данных в фрейм взятый из библиотеки pandas
    data_to_pandas - словарь состоящий из названий столбцов и списков значений, 
    которые будует помещены в соответствующий столбец
    """
    data_frame: pd.DataFrame = pd.DataFrame(data_to_pandas)
    return data_frame

def validate_timers_seconds(timers_second_list: list[int, int]):
    """
    Функция для преобразования списка секунд, которые в отдельности были насчитаны таймерами.
    При списке секунд, где у нас все нули, matplotlib при выводе выдавала ошибку, поэтому такой список,
    где все нули, я решил заменить на список, где все единицы, результат от этого не меняется.
    timers_second_list - список секунд, которые были насчитаны всеми таймерами
    """
    lists_zero: list[int, int] = []

    for timers_second in timers_second_list:
        if timers_second == 0:
            lists_zero.append(timers_second)
    
    lists_ones: list[int, int] = []

    if len(lists_zero) == len(timers_second_list):
        for one_zero in timers_second_list:
            lists_ones.append(1)

        return lists_ones

    return timers_second_list

def diagram_pie_show(timers_second_list: list[int, int], timers_names_list: list[str, str]):
    """
    Функция для вывода диаграммы на экран с уже заготовленными данными:
    timers_second_list - список секунд, которые были насчитаны таймерами в отдельности
    timers_names_list - список названий таймеров
    """

    timers_second_list: list[int, int] = validate_timers_seconds(timers_second_list)

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