
import json

from timer.class_timer import Timer
from .utils import get_json_path_save
from exception.json_exception import JsonFileError

def create_data_to_json(all_timers_dict: dict[str, Timer]):
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
    save = True
    try:
        with open(json_path, "w") as file_json:
            # Делаем превращение нашего словаря данных в json и сохранение этих данных в файл
            json.dump(dict_data_to_json, file_json, ensure_ascii=False)
    except JsonFileError:
        save = False

    return save

    


def save_data_to_json(all_timers_dict):
    # Создаем словарь данных, который должен будет пойти в json
    dict_data_to_json = create_data_to_json(all_timers_dict)
    print()
    # Получаем путь, куда нужно сохранить данные из программы
    path = get_json_path_save()
    # Делаем сохранение словаря данных (будет преобразовн в json) по указаному пути
    save_to_file: bool = save_dict_data_json(dict_data_to_json, path)

    if save_to_file:
        print("Сохранение в файл json удалось.")
    else:
        print("Сохранение в файл json не удалось.")

