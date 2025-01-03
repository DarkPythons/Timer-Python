"""
Модуль, где лежат основные функции для загрузки прогресса программы из json файла
"""

import json
from timer.class_timer import Timer
from .utils import get_json_path_load
from config import SEP
from times.times import delay_actions
from exception.json_exception import JsonFileError



def get_data_from_json(path_json: str):
    
    get_data = False
    json_data = {}

    default_path = f"..{SEP}save_programms{SEP}save.json"



    with open(path_json, "r") as file_open:
        json_data = json.load(file_open)



    return dict(json_data)


def configurate_timers_info(dict_from_json):
    timers_informaion_dict = {}

    for one_dict_information in dict_from_json.values():
        # print(one_dict_information)

        name_timer = one_dict_information.get("name_timer")
        seconds_count_in_timer = one_dict_information.get("seconds_count_in_timer")
        number_timer = one_dict_information.get("number_timer")
        
        # print(name_timer, seconds_count_in_timer, number_timer)

        # Если вся информация есть
        if name_timer != None and seconds_count_in_timer != None and number_timer != None:
            # Делаем создание нового объекта таймера
            one_object_timer = Timer(name_timer, seconds_count_in_timer, number_timer)
            # Делаем добавление нового объекта таймера в словарь всех таймеров
            timers_informaion_dict.update({name_timer : one_object_timer})

        # Если хотя бы одного пункта нет
        else:
            print("Загрузить объект таймера не удалось, повреждение данных в файле, проверьте свой json файл.")

    return timers_informaion_dict


def load_data_from_json():
    # Получаем путь, куда нужно сохранить данные из программы
    path = get_json_path_load()
    if path:
        # Делаем получение словаря данных, который пришел из json файла
        dict_from_json = get_data_from_json(path)
        timers_informaion = configurate_timers_info(dict_from_json)
        return timers_informaion
    else:
        return