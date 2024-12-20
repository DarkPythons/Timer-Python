"""
Главный файл через который у нас будет происходить запуск всей программы таймера
python timer_main.py
python3 timer_main.py
"""

import time

from text import start_message, line, input_command_user, help_user_text
from class_timer import TimerClass
from function_timers import *

# Словарь который будет содержать все объекты таймера в виде:
# Название таймера - объект таймера
all_timers_dict: dict = {}

# Приветствие с пользователем
print(start_message)
print(line)

input_user_message: str = input(input_command_user)

while input_user_message not in ("q", "quit",):

    # Если пользователь хочет создать новый объект таймера
    if input_user_message in ("c", "create",):
        name_timer = input("Введите название таймера: ")
        timers_dict: dict[str, TimerClass] = create_new_timer(name_timer)
        all_timers_dict.update(timers_dict)
        print(f"Таймер '{name_timer}' был создан")

    # Если пользователь хочет запустить таймер
    if input_user_message in ("s", "start",):
        timers_object_list: list[TimerClass] = get_timers_list(all_timers_dict)
        if timers_object_list:
            name_number_timer: str = get_name_number_task(timers_object_list, "его запуска")
            numbers_timers, names_timers = get_lists_numbers_and_names_timers(timers_object_list)

            # Если пользователь ввёл название таймера которое есть в списке названий
            if name_number_timer in names_timers:
                timer_object: TimerClass = all_timers_dict[name_number_timer]
                timer_object.start()

            # Если пользователь ввёл название таймера которое есть в списке номеров
            elif name_number_timer in numbers_timers:
                number_timer = int(name_number_timer)
                timer_object: TimerClass = get_timer_by_number(timers_object_list, number_timer)
                timer_object.start()

            else:
                print("Названия или номера с таким таймером просто нет, обратитесь к команде create.")

    # Если пользователь хочет удалить таймер
    elif input_user_message in ("d", "delete",):
        timers_object_list = get_timers_list(all_timers_dict)
        if timers_object_list:
            name_number_timer = get_name_number_task(timers_object_list, "ЕГО УДАЛЕНИЯ")
            numbers_timers, names_timers = get_lists_numbers_and_names_timers(timers_object_list)


            # Если пользователь ввёл название таймера которое есть в списке названий
            if name_number_timer in names_timers:
                del all_timers_dict[name_number_timer]
                print(f"Таймер '{name_number_timer}' был удален")

            # Если пользователь ввёл название таймера которое есть в списке номеров
            elif name_number_timer in numbers_timers:
                number_timer = int(name_number_timer)
                timer_object: TimerClass = get_timer_by_number(timers_object_list, number_timer)
                name_timer = timer_object.name_timer
                del all_timers_dict[name_timer]
                print(f"Таймер '{name_timer}' был удален")
                
            else:
                print("Названия или номера с таким таймеров просто нет, обратитесь к команде create.")   

    # Если пользователь хочет сбросить таймер
    if input_user_message in ("r", "restart",): 
        timers_object_list = get_timers_list(all_timers_dict)
        if timers_object_list:
            name_number_timer = get_name_number_task(timers_object_list, "ЕГО СБРОСА")
            numbers_timers, names_timers = get_lists_numbers_and_names_timers(timers_object_list)

            # Если пользователь ввёл название таймера которое есть в списке названий
            if name_number_timer in names_timers:
                timer_object =  all_timers_dict[name_number_timer]
                timer_object.restart()

            # Если пользователь ввёл название таймера которое есть в списке номеров
            elif name_number_timer in numbers_timers:
                number_timer = int(name_number_timer)
                timer_object: TimerClass = get_timer_by_number(timers_object_list, number_timer)
                timer_object.restart()

            else:
                print("Названия или номера с таким таймеров просто нет, обратитесь к команде create.")   
    # Если пользователь хочет получить список имён всех таймеров
    elif input_user_message in ("list", "ls",):
        timers_object_list = get_timers_list(all_timers_dict)

        if timers_object_list:
            prints_list_timers(timers_object_list)
            time.sleep(1)


    # Если пользователь хочет получить информацию обо всех таймерах
    elif input_user_message in ("ia", "info all", "all",):
        timers_object_list = get_timers_list(all_timers_dict)
        view_all_information_timers(timers_object_list)

    # Если пользователь хочет получить информацию по конкретному таймеру
    elif input_user_message in ("it", "info timer", "timer",):
        timers_object_list = get_timers_list(all_timers_dict)
        if timers_object_list:
            name_number_timer = get_name_number_task(timers_object_list, "получение информации о нём")
            numbers_timers, names_timers = get_lists_numbers_and_names_timers(timers_object_list)

            # Если пользователь ввёл название таймера которое есть в списке названий
            if name_number_timer in names_timers:
                timer_object =  all_timers_dict[name_number_timer]
                timer_object.print_information()

            # Если пользователь ввёл название таймера которое есть в списке номеров
            elif name_number_timer in numbers_timers:
                number_timer = int(name_number_timer)
                timer_object: TimerClass = get_timer_by_number(timers_object_list, number_timer)
                timer_object.print_information()

            else:
                print("Названия или номера с таким таймеров просто нет, обратитесь к команде create.")
    # Если пользователь запросил справку по командам    
    elif input_user_message in ("h", "help", "помощь",):
        print(help_user_text)

    input_user_message = input(input_command_user)

# question_diagram = input("Сделать вывод диаграммы, которая будет содержать результаты работы таймера?[N/y]: ")