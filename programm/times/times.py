"""Модуль, который содержит основные функции для работы с получением времени"""

import datetime
import time

from config import TIME_DELAY, TEXT_DELAY

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

def delay_actions() -> str:
    """
    Функция, для задрежки действий пользователя, то есть чтобы была иллюзия загрузки
    """

    part_of_delay = TIME_DELAY / 3

    for index in range(0, 3):
        print(TEXT_DELAY, end=" ", flush=True)
        time.sleep(part_of_delay)
    
    print("")

    