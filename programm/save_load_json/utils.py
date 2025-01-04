"""
Содержит основные общие функции для загрузки прогресса и его сохранения в файл json.
validate_user_path_json - валидация пути до json файла, где будут лежать данные прогресса.
"""

import json

from exception.json_exception import JsonReadFileError, JsonWriteFileError
from json.decoder import JSONDecodeError

def validate_user_path_json(user_path: str) -> bool:
    """
    Функция для валидации пути к файлу json и самого файла json при помощи попытки его чтения.
    user_path - путь и сам файл, который нужно проверить на корректность
    """
    valide: bool = True

    len_path: int = len(user_path)
    if len_path < 6:
        valide = False
    if len_path > 6:
        if user_path[-5:] != ".json":
            valide = False
    # Если путь всё ещё валиден, нужно делать ещё проверку
    if valide:
        try:

            with open(user_path, "a") as file:
                file.write("")

            with open(user_path, "r") as file:
                json.load(file)

        except (JsonReadFileError, JsonWriteFileError, FileNotFoundError, JSONDecodeError):
            valide = False

    return valide


