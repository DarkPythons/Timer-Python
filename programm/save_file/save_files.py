"""
Содержит основные функции для записи фрейма данных (табличные данные) в файл txt.
save_dataframe_to_file - функция для сохранения фрейма данных в указанный пользователем файл.
"""

import pandas as pd

from .utils import get_file_path


def save_dataframe_to_file(pandas_dataframe: pd.DataFrame) -> bool:
    """
    Делает сохранения данных (которые взяты как итог работы программы) в файл с расширением txt.
    pandas_dataframe - объект типа данных DataFrame, который при преобразовании и записи в строчном виде
    выдает строку. Содержит итоги работы программы.
    """
    file_path = get_file_path()
    string_dataframe: str = str(pandas_dataframe)

    # Открытие файла по его пути и сохранение нашего фрейма в виде строки
    with open(file_path, "a") as file_open:
        file_open.write(string_dataframe)
        file_open.write("\n")
        file_open.write("\n")
    