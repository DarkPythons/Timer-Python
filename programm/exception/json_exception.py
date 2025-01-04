"""
Модуль с исключениями, которые возникают в ходе работы с json файлами
JsonFileError - Исключение работы с файлами json.
JsonReadFileError - Исключение чтения данных из json файлов.
JsonWriteFileError - Исключение записи данных в json файл.
"""

from json.decoder import JSONDecodeError

class JsonFileError(FileNotFoundError, PermissionError):
    """Базовое исключение связянное с файлами json"""
    pass

class JsonReadFileError(JSONDecodeError, JsonFileError):
    """Исключение связанное с неправильным или невозможностью чтения json файла"""
    pass

class JsonWriteFileError(JSONDecodeError, JsonFileError):
    """Исключение связанное с невозможностью открытия или записи данных в json файл"""
    pass