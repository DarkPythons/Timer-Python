"""
Главный файл через который у нас будет происходить запуск всей программы таймера
python timer_main.py
python3 timer_main.py
"""

import pandas as pd

from text import line, start_message, input_command_user, help_user_text, command_not_found
from times.times import delay_actions, delay_actions_finish, get_padding_and_line
from timer.class_timer import Timer 
from timer.function_timers import (
    create_new_timer, get_timers_list, get_name_number_task, 
    get_lists_numbers_and_names_timers, get_timer_by_number, prints_list_timers,
    view_all_information_timers, configure_data_to_pandas)
from exception.diagram_exception import ViewDiagrammError
from diagram.show_diagram import show_diagram
from diagram.save_diagram import save_diagram_to_file
from save_load_json.save_programm import save_data_to_json
from save_load_json.load_programm import load_data_from_json
from diagram.utils import  create_pandas_object, get_file_path_diagram
from save_file.save_files import save_dataframe_to_file


# Словарь который будет содержать все объекты таймера в виде:
# Название таймера - объект таймера
all_timers_dict: dict = {}

ANSWERS_YES = ("Y", "y", "yes", "Yes", "yEs", "YES", "да", "Да", "дА", "ДА", "+")

# Приветствие с пользователем
print(start_message)
delay_actions_finish()

print("\n")

question_load_json = input("Хотите загрузить прогресс работы с таймерами из json файла [N/y]: ")


if question_load_json in ANSWERS_YES:
    informations_timers_from_json = load_data_from_json()
    if informations_timers_from_json:
        print("Загрузка данных из json файла прошла успешно, вы можете посмотреть загруженную информацию при помощи команды ia.")
        all_timers_dict = informations_timers_from_json
    elif informations_timers_from_json == {}:
        print("Загрузка данных из json файла прошла успешно, но в нём не было информации.")

# TODO: сделать возможность загрузки прогресса из json файла

input_user_message: str = input(input_command_user)

while input_user_message not in ("q", "quit",):

    # Если пользователь хочет создать новый объект таймера
    if input_user_message in ("c", "create",):
        name_timer = input("Введите название таймера: ")
        timers_dict: dict[str, Timer] = create_new_timer(name_timer)
        all_timers_dict.update(timers_dict)
        print(f"Таймер '{name_timer}' был создан")

    # Если пользователь хочет запустить таймер
    elif input_user_message in ("s", "start",):
        print("Список всех доступных таймеров: ")
        timers_object_list: list[Timer] = get_timers_list(all_timers_dict)
        if timers_object_list:
            name_number_timer: str = get_name_number_task(timers_object_list, "его запуска")
            numbers_timers, names_timers = get_lists_numbers_and_names_timers(timers_object_list)

            # Если пользователь ввёл название таймера которое есть в списке названий
            if name_number_timer in names_timers:
                timer_object: Timer = all_timers_dict[name_number_timer]
                timer_object.start()

            # Если пользователь ввёл название таймера которое есть в списке номеров
            elif name_number_timer in numbers_timers:
                number_timer = int(name_number_timer)
                timer_object: Timer = get_timer_by_number(timers_object_list, number_timer)
                timer_object.start()

            else:
                print("Названия или номера с таким таймером просто нет, обратитесь к команде create.")

    # Если пользователь хочет удалить таймер
    elif input_user_message in ("d", "delete",):
        print("Список всех доступных таймеров: ")
        timers_object_list: list[Timer] = get_timers_list(all_timers_dict)
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
                timer_object: Timer = get_timer_by_number(timers_object_list, number_timer)
                name_timer = timer_object.name_timer
                del all_timers_dict[name_timer]
                print(f"Таймер '{name_timer}' был удален")
                
            else:
                print("Названия или номера с таким таймеров просто нет, обратитесь к команде create.")   

    # Если пользователь хочет сбросить таймер
    elif input_user_message in ("r", "restart",):
        print("Список всех доступных таймеров: ")
        timers_object_list: list[Timer] = get_timers_list(all_timers_dict)
        if timers_object_list:
            name_number_timer = get_name_number_task(timers_object_list, "ЕГО СБРОСА")
            numbers_timers, names_timers = get_lists_numbers_and_names_timers(timers_object_list)

            # Если пользователь ввёл название таймера которое есть в списке названий
            if name_number_timer in names_timers:
                timer_object: Timer = all_timers_dict[name_number_timer]
                timer_object.restart()

            # Если пользователь ввёл название таймера которое есть в списке номеров
            elif name_number_timer in numbers_timers:
                number_timer = int(name_number_timer)
                timer_object: Timer = get_timer_by_number(timers_object_list, number_timer)
                timer_object.restart()

            else:
                print("Названия или номера с таким таймеров просто нет, обратитесь к команде create.")   
    # Если пользователь хочет получить список имён всех таймеров
    elif input_user_message in ("list", "ls",):
        print("Список всех доступных таймеров: ")
        timers_object_list: list[Timer] = get_timers_list(all_timers_dict)

        if timers_object_list:
            prints_list_timers(timers_object_list)


    # Если пользователь хочет получить информацию обо всех таймерах
    elif input_user_message in ("ia", "info all", "all",):
        print("Список таймеров и информации о них: ")
        timers_object_list: list[Timer] = get_timers_list(all_timers_dict)
        view_all_information_timers(timers_object_list)

    # Если пользователь хочет получить информацию по конкретному таймеру
    elif input_user_message in ("it", "info timer", "timer",):
        print("Список всех доступных таймеров: ")
        timers_object_list: list[Timer] = get_timers_list(all_timers_dict)
        if timers_object_list:
            name_number_timer = get_name_number_task(timers_object_list, "получение информации о нём")
            numbers_timers, names_timers = get_lists_numbers_and_names_timers(timers_object_list)

            # Если пользователь ввёл название таймера которое есть в списке названий
            if name_number_timer in names_timers:
                timer_object: Timer = all_timers_dict[name_number_timer]
                timer_object.print_information()

            # Если пользователь ввёл название таймера которое есть в списке номеров
            elif name_number_timer in numbers_timers:
                number_timer = int(name_number_timer)
                timer_object: Timer = get_timer_by_number(timers_object_list, number_timer)
                timer_object.print_information()

    

            else:
                print("Названия или номера с таким таймеров просто нет, обратитесь к команде create.")
    # Если пользователь запросил справку по командам    
    elif input_user_message in ("h", "help", "помощь",):
        print(help_user_text)

    # Если команды, которую ввёл пользоватеть нет
    else:
        print(command_not_found)

    delay_actions()
    input_user_message = input(input_command_user)

# Если хотя бы один таймер был создан
if all_timers_dict:

    # Значение по умолчанию, когда пользователь будет выходить из программы, у него будет выбор переопределить их
    question_save_diagram = "нет"
    question_save_file = "нет"
    question_view_diagram = "нет"
    question_save_json = "нет"

    print()
    delay_actions_finish()

    print("Итог работы программы: ")
    timers_object_list: list[Timer] = get_timers_list(all_timers_dict)
    view_all_information_timers(timers_object_list)

    delay_actions_finish()
    print("\n")

    question_save_json = input("Хотите сохранить результат работы программы в json файл, чтобы в дальнейшем восстановить работу с таймерами, которые у вас были созданы сейчас [N/y]: ")

    # Если пользователь хочет сохранить данные о работе в json файл
    if question_save_json in ANSWERS_YES:
        get_padding_and_line()
        save_data_to_json(all_timers_dict)
        

    if question_save_json in ANSWERS_YES:
        get_padding_and_line()

    print()

    question_view_diagram = input("Хотите вывести диаграмму, "
        "которая будет отображать соотношение посчитанного времени на всех таймерах [N/y]: ") 



    # Если ответ на вопрос о выводе диаграммы находится в списках да
    if question_view_diagram in ANSWERS_YES:

        try:
            show_diagram(all_timers_dict)

        except ViewDiagrammError as Error:
            print(f"К сожалению возникла ошибка при выводе диаграммы, текст ошибки: {Error}")

    if question_view_diagram in ANSWERS_YES:
        get_padding_and_line()

    print()

    question_save_diagram = input("Хотите сохранить диаграму таймеров в файл [N/y]: ")



    # Если пользователь хочет сохранить диаграмму
    if question_save_diagram in ANSWERS_YES:
        get_padding_and_line()
        print()


        file_path = get_file_path_diagram()

        # Сохраняем диаграмму в файл, передавая полученный путь до файла и состояние самой диаграммы
        save_diagram_to_file(file_path, all_timers_dict)
        print("Сохранение диаграммы в файл удалось.")

    if question_save_diagram in ANSWERS_YES:
        get_padding_and_line()
        
    print()


    question_save_file = input("Хотите сохранить результат работы программы (в виде таблицы) в файл [N/y]: ")


    # Если пользователь хочет сохранить результат работы программы в файл
    if question_save_file in ANSWERS_YES:

        get_padding_and_line()
        print()

        timers_object_list: list[Timer] = get_timers_list(all_timers_dict)
        data_pandas: dict[str, list] = configure_data_to_pandas(timers_object_list)
        dataframe_object: pd.DataFrame = create_pandas_object(data_pandas)
        save_dataframe_to_file(dataframe_object)
        print("Сохранение таблицы итогов в файл удалось")

    print()


else:
    print("Для выведения итогов программы, должен быть создан хотя бы один таймер.")



print("Досвидания.")