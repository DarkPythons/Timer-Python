"""
Содержит нужные функции для работы программы
get_terminal_user_width - получить ширину терминала, с которого была запущена программа
"""

import os

def get_terminal_user_width():
    """
    Делает получение ширины терминала, с которого была запущена программа, 
    используется для красивого вывода строки ожидания.
    """
    width = 100
    # Получаем размеры терминала по оси x и y
    sizes_terminal = os.get_terminal_size()
    try:
        # Получаем значение по оси x, то есть ширину
        width_terminal = sizes_terminal[0]
    except IndexError:
        pass
    else:
        width = width_terminal
    return width
