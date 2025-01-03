"""
Содержит функции для сохранения прогресса программы в файл json.
create_data_to_json - создать словарь, который нужно будет поместить в json файл 
save_dict_data_json - сохранение словаря данных в файл json по указанному пути
get_json_path_save - получить путь до json файла, куда нужно сделать сохранение прогресса
"""

import json

from config import SEP
from timer.class_timer import Timer
from times.times import delay_actions
from .utils import validate_user_path_json
from exception.json_exception import JsonFileError

def create_data_to_json(all_timers_dict: dict[str, Timer]):
    """
    Создает и возвращает словарь, который нужно будет записать в json файл.
    all_timers_dict - словарь с объектами таймеров программы, из которых нужно брать информацию
    """
    dict_finish = {}
    for one_object_timer in all_timers_dict.values():
        
        number_timer = one_object_timer.number_timer
        name_timer = one_object_timer.name_timer
        seconds_count_in_timer = one_object_timer.count_second
        new_dict_timer = {
            "number_timer" : number_timer,
            "name_timer" : name_timer,
            "seconds_count_in_timer" : seconds_count_in_timer
        }
        dict_finish.update({number_timer : new_dict_timer})
    return dict_finish

def save_dict_data_json(dict_data_to_json, json_path):
    """
    Сохраняет словарь из create_data_to_json в файл json по определенному пути.
    dict_data_to_json - словарь, который нужно сохранить
    json_path - путь до json файла
    """
    save = True
    try:
        with open(json_path, "w") as file_json:
            # Делаем превращение нашего словаря данных в json и сохранение этих данных в файл
            json.dump(dict_data_to_json, file_json, ensure_ascii=False)
    except JsonFileError:
        save = False

    return save

def get_json_path_save() -> str:
    """
    Функция для получения пути куда сохранять наш результат работы программы в виде json
    Будет делать запрос пользователю, чтобы он ввёл путь, если он его не вводит, или
    вводит некорректный путь, то возвращается путь по умолчанию.
    """
    path = f"..{SEP}save_programms{SEP}save.json"

    print(f"Пример такого пути: C:{SEP}Users{SEP}User{SEP}Desktop{SEP}my_save_prog.json")
    user_path = input("Введите путь и название файла (с расширением json), " 
        "куда бы вы хотели записать результаты (не обязательно): ")

    delay_actions()
    
    valide_path: bool = validate_user_path_json(user_path)
    # Если путь который ввёл пользователь валиден
    if valide_path:
        print(f"Путь '{user_path}' валиден, сохранение результатов пройдёт в него.")
        path = user_path
    else:
        print(f"Путь '{user_path}' не валиден, сохранение пройдёт в файл по умолчанию, ")
        print(f"по пути: '{path}'")
        
    return path

