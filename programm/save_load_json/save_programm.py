
import json
from timer.class_timer import Timer
from config import SEP
from times.times import delay_actions
from exception.json_exception import JsonFileError

def create_data_to_json(all_timers_dict: dict[str, Timer]):
    dict_finish = {}
    for one_object_timer in all_timers_dict.values():
        
        number_timer = one_object_timer.timer_object_count
        name_timer = one_object_timer.name_timer
        seconds_count_in_timer = one_object_timer.count_time
        new_dict_timer = {
            "number_timer" : number_timer,
            "name_timer" : name_timer,
            "seconds_count_in_timer" : seconds_count_in_timer
        }
        dict_finish.update({number_timer : new_dict_timer})
    return dict_finish

def save_dict_data_json(dict_data_to_json, json_path):
    save = True
    try:
        with open(json_path, "w") as file_json:
            # Делаем превращение нашего словаря данных в json и сохранение этих данных в файл
            json.dump(dict_data_to_json, file_json)
    except JsonFileError:
        save = False

    return save

    

def validate_user_path_json(user_path):
    valide = True
    len_path = len(user_path)
    if len_path < 6:
        valide = False
    if len_path > 6:
        if user_path[-5:] != ".json":
            valide = False
    try:
        with open(user_path, "a") as file:
            file.write("")
    except (PermissionError, FileNotFoundError):
        valide = False

    return valide

def get_json_path() -> str:
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

def save_data_to_json(all_timers_dict):
    # Создаем словарь данных, который должен будет пойти в json
    dict_data_to_json = create_data_to_json(all_timers_dict)
    print()
    # Получаем путь, куда нужно сохранить данные из программы
    path = get_json_path()
    # Делаем сохранение словаря данных (будет преобразовн в json) по указаному пути
    save_to_file: bool = save_dict_data_json(dict_data_to_json, path)

    if save_to_file:
        print("Сохранение в файл json удалось.")
    else:
        print("Сохранение в файл json не удалось.")

