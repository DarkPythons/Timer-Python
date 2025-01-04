"""
Содержит основные функции для сохранения прогресса программы в файл json.
save_data_to_json - сохранение данных в json
"""

from .save_utils import get_json_path_save, create_data_to_json, save_dict_data_json 
from timer.class_timer import Timer

def save_data_to_json(all_timers_dict: dict[str, Timer]) -> None:
    """
    Функция для сохранения данных программы в json файл.
    all_timers_dict - словарь со всеми объектами таймеров программы, откуда и брать информацию.
    """

    # Создаем словарь данных, который должен будет пойти в json
    dict_data_to_json: dict[str, dict[str, int|str]] = create_data_to_json(all_timers_dict)
    print()
    # Получаем путь, куда нужно сохранить данные из программы
    path: str = get_json_path_save()
    # Делаем сохранение словаря данных (будет преобразовн в json) по указаному пути
    save_to_file: bool = save_dict_data_json(dict_data_to_json, path)

    if save_to_file:
        print("Сохранение в файл json удалось.")
    else:
        print("Сохранение в файл json не удалось.")

