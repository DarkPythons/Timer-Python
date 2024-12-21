:: Файл для запуска программы таймера

:: Убираем лишний вывод в терминале
@echo off

:: Ставим кодовую страницу терминала на UTF-8
chcp 65001

:: Называем программу терминала как: Таймер
title Таймер

echo Нажмите любую клавишу далее, чтобы начать установку пакетного менеджера
pause

:: Установка пакетного менеджера poetry
pip install poetry && echo poetry пакетный менеджер был установлен (или он у вас уже был)

:: Установка всех нужных зависимостей в окружение .venv
poetry install && echo Все зависимости установлены

echo Ожидайте запуска программы...

cd programm

set program_start=0

if %program_start% EQU 0 (
    poetry run python main.py && set program_start=1
)

if %program_start% EQU 0 (
    poetry run python3 main.py && set program_start=1
)

:: Если программа отработала
if %program_start% EQU 1 (
	echo Программа завершила свою работу после того как отработала
) else (
	echo К сожалению программу не удалось запустить
)