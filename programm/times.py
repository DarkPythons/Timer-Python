"""Модуль, который содержит основные функции для работы с получением времени"""

import datetime

def get_time_today() -> str:
    """
    Функция для получения даты, когда программа рабоает, возвращает дату в формате:
    день.месяц.год
    """

    current_datetime: datetime = datetime.datetime.today()
    day: int = current_datetime.day
    month: int = current_datetime.month
    year: int = current_datetime.year

    string_datetime: str = f"{day}.{month}.{year}"
    return string_datetime