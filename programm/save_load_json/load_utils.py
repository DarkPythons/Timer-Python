"""
Содержит основные функции для загрузки прогресса программы из файла json.
get_command_by_user - делает запрос на ввод команды от пользователя, которая будет определять, 
какой путь до json файла нужно взять при загрузке прогресса
get_json_path_load - получить путь до json файла, откуда нужно загружать прогресс.
"""

from config import SEP
from times.times import delay_actions
from .utils import validate_user_path_json
from times.times import delay_actions, get_padding_and_line

def get_command_by_user(default_path: str) -> str:
    """
    Делает запрос пользователю на ввод команды, которая будет определять, по какому пути открывать
    json файл для загрузки его данных.
    default_path - путь по умолчанию, который будет предлагаться пользователю
    """
    print(f"""
Вы можете ввести новый путь до файла json, где лежит прогресс программы,
Например: C:{SEP}Users{SEP}User{SEP}Desktop{SEP}my_save_prog.json\n
Или воспользоваться доступными командами:
qj [quit json] - выйти из диалога по загрузке json файла и запустить программу без прогресса.
dp [default path] - использовать json файл по пути по умолчанию, сам путь: 
'{default_path}'
    """)

    user_command = input("-> ")
    delay_actions()
    print()
    return user_command  

def get_json_path_load() -> str:
    """
    Функция для получения пути до файла json, откуда нужно брать данные для загрузки прогресса.
    Если пользователь будет вводить неккоретный путь, у него будет полноценное окно выбора команды.
    """
    default_path = f"..{SEP}save_programms{SEP}save.json"

    print(f"Пример такого пути: C:{SEP}Users{SEP}User{SEP}Desktop{SEP}my_save_prog.json")
    user_path = input("Введите путь и название файла (с расширением json), " 
        "откуда бы вы хотели взять прогресс работы программы (не обязательно): ")
    delay_actions()
    print()
    path = ""

    # Если пользователь не захотел вводить путь до файла, то берем путь по умолчанию
    if user_path == "":
        print(f"Путь будет взят как значение по умолчанию, то есть '{default_path}'")
        user_path = default_path

    # Пока нет итогового пути
    while not path:
        valide_path: bool = validate_user_path_json(user_path, "load")

        if valide_path:
            print(f"Путь '{user_path}' валиден, загрузка прогресса пройдет из него.")
            get_padding_and_line()
            print()
            path = user_path
        
        else:
            print(f"Путь '{user_path}' или данные из этого файла не валидны, выберите одно из следующих действий: ")
            user_command = get_command_by_user(default_path)

            # Если пользователь передумал загружать прогресс из json файла
            if user_command in ("qj", "quit json"):
                print("Выход из диалогового окна загрузки прогресса.")
                get_padding_and_line()
                break
            # Если пользователь хочет использовать путь по умолчанию
            if user_command in ("dp", "default path"):
                print("Взят путь до файла json по умолчанию.")
                path = default_path
            # Если ввели другой путь до json файла (после чего его проверка на валидность повторится)
            else:
                user_path = user_command

    return path