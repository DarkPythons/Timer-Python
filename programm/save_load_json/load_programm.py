"""
Содержит основные функции для получения данных из json файла и их загрузки в программу.
get_data_from_json - сделать чтение файла json и возвращение данных оттуда в виде словаря
configurate_timers_info - сделать распаршивание словаря, который вернулся на нужные данные
и создание новых таймеров на основании этих данных
load_data_from_json - сделать загрузку данных из файла json
"""

import json

from timer.class_timer import Timer
from .load_utils import get_json_path_load


def get_data_from_json(path_json: str) -> dict[str, dict[str, int|str]]:
    """
    Делает чтение файла json по указанному пути и возврат данных оттуда в виде словаря
    path_json - путь до самого json файла
    """
    json_data = {}
    with open(path_json, "r") as file_open:
        json_data: dict[str, dict[str, int|str]] = json.load(file_open)
    return dict(json_data)


def configurate_timers_info(dict_from_json: dict[str, dict[str, int|str]]) -> dict[str, Timer]:
    """
    Делает преобразование словаря данных, который вернулся из json в обычные данные и на их
    основании создает новые объекта таймеров, которые помещаются в конечный словарь.
    dict_from_json - словарь, который вернулся из json файла
    """
    timers_informaion_dict = {}

    for one_dict_information in dict_from_json.values():
        name_timer: str = one_dict_information.get("name_timer")
        seconds_count_in_timer: int = one_dict_information.get("seconds_count_in_timer")
        number_timer: int = one_dict_information.get("number_timer")
        
        # Если вся информация есть
        if name_timer != None and seconds_count_in_timer != None and number_timer != None:
            # Делаем создание нового объекта таймера
            one_object_timer: Timer = Timer(name_timer, seconds_count_in_timer, number_timer)
            # Делаем добавление нового объекта таймера в словарь всех таймеров
            timers_informaion_dict.update({name_timer : one_object_timer})

        # Если хотя бы одного пункта нет
        else:
            print("Загрузить объект таймера не удалось, повреждение данных в файле, проверьте свой json файл.")

    return timers_informaion_dict


def load_data_from_json() -> dict[str, Timer]:
    """
    Функция для загрузки данных из json файла, возвращает уже готовый словарь с объектами таймеров.
    """
    # Получаем путь, куда нужно сохранить данные из программы
    path: str = get_json_path_load()
    if path:
        # Делаем получение словаря данных, который пришел из json файла
        dict_from_json: dict[str, dict[str, int|float]] = get_data_from_json(path)
        timers_informaion: dict[str, Timer] = configurate_timers_info(dict_from_json)
        return timers_informaion
    else:
        return