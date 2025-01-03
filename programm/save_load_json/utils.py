from timer.class_timer import Timer
from config import SEP
from times.times import delay_actions
from exception.json_exception import JsonFileError
import json

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

        with open(user_path, "r") as file:
            json.load(file)

    except (PermissionError, FileNotFoundError, json.decoder.JSONDecodeError):
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

def get_json_path_load() -> str:
    """
    Функция для получения пути куда сохранять наш результат работы программы в виде json
    Будет делать запрос пользователю, чтобы он ввёл путь, если он его не вводит, или
    вводит некорректный путь, то возвращается путь по умолчанию.
    """
    default_path = f"..{SEP}save_programms{SEP}save.json"

    print(f"Пример такого пути: C:{SEP}Users{SEP}User{SEP}Desktop{SEP}my_save_prog.json")
    user_path = input("Введите путь и название файла (с расширением json), " 
        "откуда бы вы хотели взять прогресс работы программы (не обязательно): ")

        

    delay_actions()

    path = ""

    if user_path == "":
        print(f"Путь будет взять как значение по умолчанию, то есть '{default_path}'")
        user_path = default_path

    # Пока нет итогового пути
    while not path:
        valide_path: bool = validate_user_path_json(user_path)

        if valide_path:
            print(f"Путь '{user_path}' валиден, загрузка прогресса пройдет из него.")
            path = user_path
        
        else:
            print(f"Путь '{user_path}' или данные из этого файла не валидны, выберите одно из следующих действий: ")
            print(f"""
Вы можете ввести новый путь до файла json, где лежит прогресс программы,
Например: C:{SEP}Users{SEP}User{SEP}Desktop{SEP}my_save_prog.json
Или воспользоваться доступными командами:
qj [quit json] - выйти из диалога по загрузке json файла и запустить программу без прогресса.
dp [default path] - использовать json файл по пути по умолчанию, сам путь: 
{default_path}
            """)

            user_command = input("-> ")

            # Если пользователь хочет выйти из загрузки прогресса из json файла
            if user_command in ("qj", "quit json"):
                break
            # Если пользователь хочет использовать путь по умолчанию
            if user_command in ("dp", "default path"):
                path = default_path
            # Если ввели другой путь до json файла
            else:
                user_path = user_command

    return path