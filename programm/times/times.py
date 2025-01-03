"""
Содержит функции для работы со временем
get_time_today - получить день, месяц и год в формате: dd.mm.yyyy
delay_actions - сделать задержку и вывод текста задержки
delay_actions_finish - сделать задержку и красивый вывод текста задержки на всю ширину терминала
get_padding_and_line - сделать отсупы для красивой задержки
"""


import datetime
import time

from config import TIME_DELAY, TEXT_DELAY, LINE_SIZE, TEXT_DELAY_EXIT

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


def delay_actions_finish():

    part_of_delay = TIME_DELAY / LINE_SIZE

    for index in range(0, LINE_SIZE):
        print(TEXT_DELAY_EXIT, end="", flush=True)
        time.sleep(part_of_delay)


def get_padding_and_line():
    print()
    delay_actions_finish()
    print()