"""
Содержит основные функции для загрузки прогресса и его сохранения в файл json.
validate_user_path_json - валидация пути до json файла, где будут лежать данные прогресса.
get_json_path_save - получить путь до json файла, куда нужно сделать сохранение прогресса
get_command_by_user - делает запрос на ввод команды от пользователя, которая будет определять, 
какой путь до json файла нужно взять при загрузке прогресса
get_json_path_load - получить путь до json файла, откуда нужно загружать прогресс.
"""

import json

from config import SEP
from times.times import delay_actions
from exception.json_exception import JsonReadFileError, JsonWriteFileError

def validate_user_path_json(user_path):
    """
    Функция для валидации пути к файлу json и самого файла json при помощи попытки его чтения.
    user_path - путь и сам файл, который нужно проверить на корректность
    """
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

        with open(user_path, "r") as file:
            json.load(file)

    except (JsonReadFileError, JsonWriteFileError):
        valide = False

    return valide

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


def get_command_by_user(default_path):
    """
    Делает запрос пользователю на ввод команды, которая будет определять, по какому пути открывать
    json файл для загрузки его данных.
    default_path - путь по умолчанию, который будет предлагаться пользователю
    """
    print(f"""
Вы можете ввести новый путь до файла json, где лежит прогресс программы,
Например: C:{SEP}Users{SEP}User{SEP}Desktop{SEP}my_save_prog.json
Или воспользоваться доступными командами:
qj [quit json] - выйти из диалога по загрузке json файла и запустить программу без прогресса.
dp [default path] - использовать json файл по пути по умолчанию, сам путь: 
{default_path}
    """)

    user_command = input("-> ")  
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

    path = ""

    # Если пользователь не захотел вводить путь до файла, то берем путь по умолчанию
    if user_path == "":
        print(f"Путь будет взят как значение по умолчанию, то есть '{default_path}'")
        user_path = default_path

    # Пока нет итогового пути
    while not path:
        valide_path: bool = validate_user_path_json(user_path)

        if valide_path:
            print(f"Путь '{user_path}' валиден, загрузка прогресса пройдет из него.")
            path = user_path
        
        else:
            print(f"Путь '{user_path}' или данные из этого файла не валидны, выберите одно из следующих действий: ")
            user_command = get_command_by_user(default_path)

            # Если пользователь передумал загружать прогресс из json файла
            if user_command in ("qj", "quit json"):
                break
            # Если пользователь хочет использовать путь по умолчанию
            if user_command in ("dp", "default path"):
                path = default_path
            # Если ввели другой путь до json файла (после чего его проверка на валидность повторится)
            else:
                user_path = user_command

    return path