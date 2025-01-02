"""Модуль, который содержит основные функции для сохранения результатов работы программы в файл."""

import pandas as pd

from .utils import get_file_path


def save_dataframe_to_file(pandas_dataframe: pd.DataFrame) -> bool:
    file_path = get_file_path()
    string_dataframe: str = str(pandas_dataframe)

    # Открытие файла по его пути и сохранение нашего фрейма в виде строки
    with open(file_path, "a") as file_open:
        file_open.write(string_dataframe)
        file_open.write("\n")
        file_open.write("\n")
    