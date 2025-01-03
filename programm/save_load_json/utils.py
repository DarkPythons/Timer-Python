"""
Содержит основные общие функции для загрузки прогресса и его сохранения в файл json.
validate_user_path_json - валидация пути до json файла, где будут лежать данные прогресса.
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


