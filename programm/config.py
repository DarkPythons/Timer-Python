"""Модуль с настройками работы программы в целом."""

import os

from utils import get_terminal_user_width

# Количество "-" при начальном отступе
LINE_SIZE: int = get_terminal_user_width()

# Использовать текст со смайликами
SMILE_TEXT = False

# Задержка перед действиями 
TIME_DELAY = 1.8

# Текст задержки (один символ, программа будет выводить этот один символ три раза)
TEXT_DELAY = "."

# Текст задержки, при выходе из программы (один символ)
TEXT_DELAY_EXIT = "-"

# Разделитель, который нужно использовать для навигации
SEP = os.sep