"""
Главный файл через который у нас будет происходить запуск всей программы таймера
python timer_main.py
python3 timer_main.py
"""

from times import delay_actions
from exception import ViewDiagrammError
from text import start_message, line, input_command_user, help_user_text, command_not_found
from class_timer import Timer
from function_timers import *
from function_diagram import (
    show_diagram, create_pandas_object, get_file_path_diagram, save_diagram_to_file
)
from function_files import save_dataframe_to_file

# Словарь который будет содержать все объекты таймера в виде:
# Название таймера - объект таймера
all_timers_dict: dict = {}

# Приветствие с пользователем
print(start_message)
print(line)

delay_actions()

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
        print("Список всех доступных таймеров: ")
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

answer_yes = ["Y", "y", "yes", "Yes", "yEs", "YES", "да", "Да", "дА", "ДА", "+"]

print(line)

question_diagram = input("Хотите вывести диаграмму, "
    "которая будет отображать соотношение посчитанного времени на всех таймерах [N/y]: ") 

delay_actions()

# Если ответ на вопрос о выводе диаграммы находится в списках да
if question_diagram in answer_yes:
    if all_timers_dict:
        try:
            show_diagram(all_timers_dict)

        except ViewDiagrammError as Error:
            print(f"К сожалению возникла ошибка при выводе диаграммы, текст ошибки: {Error}")
    else:
        print("К сожалению у вас нет таймеров, чтобы делать вывод диаграммы основании их данных")

else:
    print("Продолжим.")

question_save_diagram = "нет"

# Если диаграмма была выведена пользователю
if question_diagram in answer_yes:
    # Если у пользователя есть хотя бы один таймер
    if all_timers_dict:
        question_save_diagram = input("Хотите сохранить выведенную диаграму в файл [N/y]: ")
        delay_actions()

if question_diagram in answer_yes:
    # Если пользователь хочет сохранить диаграмму
    if question_save_diagram in answer_yes:
        file_path = get_file_path_diagram()
        delay_actions()
        # Сохраняем диаграмму в файл, передавая полученный путь до файла и состояние самой диаграммы
        save_diagram_to_file(file_path, all_timers_dict)
        print("Диаграмма была сохранена\n")

question_file = input("Хотите сохранить результат работы программы (в виде таблицы) в файл [N/y]: ")

delay_actions()

# Если ответ на вопрос о сохранении результата программы в файл да
if question_file in answer_yes:
    if all_timers_dict:
        timers_object_list: list[Timer] = get_timers_list(all_timers_dict)
        data_pandas: dict[str, list] = configure_data_to_pandas(timers_object_list)
        dataframe_object: pd.DataFrame = create_pandas_object(data_pandas)
        save_dataframe_to_file(dataframe_object)
    else:
        print("К сожалению у вас нет таймеров, чтобы делать вывод результатов в файл")
else:
    print("Продолжим.")


delay_actions()
print("Досвидания.")