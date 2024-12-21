"""
Модуль, который содержит основные функции для работы с диаграммой
"""

import matplotlib.pyplot as plt
import pandas as pd

from class_timer import Timer
from function_timers import get_timers_list, get_list_names_timers, get_list_seconds_timers
from times import get_time_today

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
    При списке секунд, где у нас все нули, matplotlib при выводе выдавала ошибку, 
    поэтому такой список,
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

def create_diagram_object(timers_second_list: list[int, int], timers_names_list: list[str, str]) -> plt:
    """
    Функция для создания объекта диаграммы с уже заготовленными данными:
    timers_second_list - список секунд, которые были насчитаны таймерами в отдельности
    timers_names_list - список названий таймеров
    Возвращает объект типа данных plt
    """

    timers_second_list: list[int, int] = validate_timers_seconds(timers_second_list)

    # Задаем название диаграммы
    plt.title("Соотношение времени и определенных задач.")
    # Создаем объект круговой диаграммы
    plt.pie(x=timers_second_list, labels=timers_names_list, autopct="%1.1f%%", startangle=180)
    # У круговой диаграммы включаем разделение по частям как у пирога
    plt.axis("equal")

    return plt


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

def validate_user_path_diag(user_path: str) -> bool:
    """
    Функция для проверки пути, который ввёл пользователь, 
    куда нужно будет сохранять диаграмму
    user_path - пользовательский путь
    """

    valide = True
    len_path = len(user_path)

    # Проверка на длину пути
    if len_path < 5:
        valide = False
    
    # Проверка на корректное окончание пути, то есть расширение файла
    if len_path > 5:
        if user_path[-4:] != ".png":
            valide = False
    
    # Попытка открыть файл и сделать запись
    try:
        with open(user_path, "a") as file:
            file.write(0x10)
    except (PermissionError, FileNotFoundError):
        valide = False

    return valide

def get_file_path_diagram() -> str:
    """Функция для получения пути до файла, куда нужно будет сохранить диаграмму"""
    today_time: str = get_time_today()
    path = f"..\\data_program\\{today_time}_diagram.png"

    print(r"Пример такого пути: C:\Users\User\Desktop\diagram.png")

    user_path = input("Введите путь и название файла, "
        "куда бы вы хотели сохранить диаграмму (не обязательно): ")

    valide_path: bool = validate_user_path_diag(user_path)

    # Если путь, который ввёл пользователь валиден
    if valide_path:
        print(f"Путь '{user_path}' валиден, сохранение диаграммы пройдёт в него.")
        path = user_path
    else:
        print(f"Путь '{user_path}' не валиден, сохранение диаграммы пройдёт в файл по умолчанию, ")
        print(f"по пути: '{path}'")
    
    return path

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