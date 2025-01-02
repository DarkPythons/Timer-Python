
from config import SEP
from times.times import get_time_today, delay_actions


def validate_user_path(user_path: str) -> bool:
    """
    Функция для валидации пути, который ввёл пользователь
    user_path - путь, который нужно проверить, то есть который ввёл пользователь
    """

    valide = True
    len_path = len(user_path)
    if len_path < 5:
        valide = False
    if len_path > 5:
        if user_path[-4:] != ".txt":
            valide = False
    try:
        with open(user_path, "a") as file:
            file.write("")
    except (PermissionError, FileNotFoundError):
        valide = False

    return valide

def get_file_path() -> str:
    """
    Функция для получения пути куда сохранять наш результат
    Будет делать запрос пользователю, чтобы он ввёл путь, если он его не вводит, или
    вводит некорректный путь, то возвращается путь по умолчанию.
    """
    today_time: str = get_time_today()
    path = f"..{SEP}..{SEP}data_program{SEP}{today_time}_timer_data.txt"

    print(f"Пример такого пути: C:{SEP}Users{SEP}User{SEP}Desktop{SEP}my_prod.txt")
    user_path = input("Введите путь и название файла, " 
        "куда бы вы хотели записать результаты (не обязательно): ")

    delay_actions()
    
    valide_path: bool = validate_user_path(user_path)
    # Если путь который ввёл пользователь валиден
    if valide_path:
        print(f"Путь '{user_path}' валиден, сохранение результатов пройдёт в него.")
        path = user_path
    else:
        print(f"Путь '{user_path}' не валиден, сохранение пройдёт в файл по умолчанию, ")
        print(f"по пути: '{path}'")
        
    return path