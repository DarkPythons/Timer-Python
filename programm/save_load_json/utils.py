"""
Содержит основные общие функции для загрузки прогресса и его сохранения в файл json.
validate_user_path_json - валидация пути до json файла, где будут лежать данные прогресса.
"""

import json

from exception.json_exception import JsonReadFileError, JsonWriteFileError
from json.decoder import JSONDecodeError


def open_read_json_by_load(user_path: str) -> bool:
    """
    Функция для открытия, попытки чтения и записи json файла и загрузки данных из него для проверки возможности
    загрузить оттуда данные
    user_path - путь до файла json, который нужно будет открыть и проверить
    """

    valide = True

    try:
        with open(user_path, "a") as file:
            file.write("")
        with open(user_path, "r") as file:
            json.load(file)
    except (JsonReadFileError, JsonWriteFileError, FileNotFoundError, JSONDecodeError):
        valide = False

    return valide

def open_write_json_by_save(user_path: str) -> bool:
    """
    Функция для открытия и попытки записать данные в json файл для проверки возможности записи туда данных для
    сохранения прогресса программы
    user_path - путь до json файла, который нужно открыть и проверить
    """

    valide = True

    try:
        with open(user_path, "a") as file:
            file.write("")
    except (JsonReadFileError, JsonWriteFileError, FileNotFoundError, JSONDecodeError):
        valide = False

    return valide

def validate_user_path_json(user_path: str, load_or_save: str) -> bool:
    """
    Функция для валидации пути к файлу json и самого файла json при помощи попытки его чтения.
    user_path - путь и сам файл, который нужно проверить на корректность
    load_or_save - строка, которая говорит, для чего конкретно будет проверяться путь
    """
    valide: bool = True

    len_path: int = len(user_path)
    if len_path < 6:
        valide = False
    if user_path[-5:] != ".json":
        valide = False

    # Если путь до файла и сам файл нужно проверить на загрузку данных туда
    if load_or_save == "save":
        if valide:
            valide = open_write_json_by_save(user_path)

    # Если путь до файла и сам файл нужно проверить на загрузку данных оттуда
    if load_or_save == "load":
        # Если путь всё ещё валиден, нужно делать ещё проверку
        if valide:
            valide = open_read_json_by_load(user_path)

    
    return valide


