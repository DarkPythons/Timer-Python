"""
Модуль, в котором лежат основные функции и методы для работы с json файлом, где лежат итоги работы программы.
Эти итоги можно будет загружать из программы и в программу обратно,
чтобы продолжить работу с уже созданными таймерами раннее
"""
from class_timer import Timer
import json


class LoadToJson:

    def create_data_to_json(self, all_timers_dict: dict[str, Timer]):
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

    def save_dict_data_json(self, dict_data_to_json):
        json_path = "../save_programms/main.json"

        with open(json_path, "w") as file_json:
            # Делаем превращение нашего словаря данных в json и сохранение этих данных в файл
            json.dump(dict_data_to_json, file_json)


def load_data_to_json(all_timers_dict):
    json_load = LoadToJson()
    # Создаем словарь данных, который должен будет пойти в json
    dict_data_to_json = json_load.create_data_to_json(all_timers_dict)
    json_load.save_dict_data_json(dict_data_to_json)

