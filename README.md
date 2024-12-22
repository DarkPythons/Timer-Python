<p align="center">
      <img src="https://i.ibb.co/0XcwvjC/photo.jpg" alt="Timer Python" border="0" width="727">
</p>

<p align="center">
   <img alt="License badge" src="https://img.shields.io/badge/Licencse-GPL-success">
  <img alt="My text" src="https://img.shields.io/badge/my_timer-blue">
   <img alt="PyPI - Status" src="https://img.shields.io/pypi/status/pandas">
  <img alt="PyPI - Python Version" src="https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json">
</p>

## О проекте

CLI таймер создан с целью контролирования своего времени и измерения полезности его проведения. У самой программы есть много полезных функций, например:
1) Создание таймеров
2) Запуск таймеров
3) Обнуление таймеров
4) Удаление таймеров
5) Вывод информации обо всех таймерах сразу
6) Получение диаграммы с соотношением всех таймеров после выхода из программы
7) Запись полученной диаграммы соотношений времени в png файл
8) Запись результатов работы программы в файл

## Зависимости

<p>Проект как зависимости использует:</p>
<p>Пакетный менеджер: poetry</p>
<p>Библиотеки python: pandas, matplotlib</p>
<p>Увидеть зависимости проекта вы можете в файлах: pyproject.toml, requirements.txt</p>

## Настройка через poetry (pyproject.toml)


<p>После скачивания проекта с github (командой в терминале: git clone https://github.com/DarkPythons/Timer-Python.git), вы должны перейти в каталог проекта.</p>
<p>После чего вы увидите файлы проекта, всё уже настроено и готово к работе, осталось лишь установить зависимости, это можно сделать при помощи команд:</p>
<p>poetry install</p>
<p>poetry shell</p>
<p>cd programm</p>
<p>poetry run python main.py</p>


## Настройка через pip (requirements.txt)

<p>После скачивания проекта с github (командой в терминале: git clone https://github.com/DarkPythons/Timer-Python.git), вы должны перейти в каталог проекта.</p>
<p>После чего вы увидите файлы проекта, всё уже настроено и готово к работе, осталось лишь установить зависимости, это можно сделать при помощи команд:</p>
<p>python -m venv .venv</p>
<p>cd .venv/scripts</p>
<p>activate.bat</p>
<p>cd ../../</p>
<p>pip install -r requirements.txt</p>
<p>cd programm</p>
<p>python main.py</p>

## Настройка через специальные файлы

<p>После скачивания проекта с github (командой в терминале: git clone https://github.com/DarkPythons/Timer-Python.git), вы должны перейти в каталог проекта.</p>
<p>После чего вы увидите файлы проекта, всё уже настроено и готово к работе, осталось лишь установить зависимости, это можно сделать при помощи файлов:</p>
<p>Windows: Timer-Python/windows_start_program.bat</p>
<p>Linux: Timer-Python/linux_start_program.sh</p>
<p>Эти файлы устанавливают пакетный менеджер poetry, после чего, сам пакетный менеджер создает среду, устанавливает зависимости и запускает программу, которая находится по пути:</p>
<p>Timer-Python/programm/main.py</p>

## Что вы должны увидеть после запуска программы (programm/main.py):

<img src="https://s3.radikal.cloud/2024/12/22/start57c01de91a59d41c.png" alt="start57c01de91a59d41c.png" border="0" />

## Конфигурация (Timer-Python/programm/config.py)
Можно сделать специальную настройку под себя таких параметров как:
1) Использование текста, где будут использоваться смайлики при общении с пользователем (по умолчанию False)
2) Задержка между действиями пользователя (по умолчанию 1.8 секунды)
3) Текст при ожидании загрузки (по умолчанию ".")


## Примеры команд и их вывода

### Получение справки по командам (команда help (или h))

<img src="https://s3.radikal.cloud/2024/12/22/helpaaddbce2115bd8cd.png" alt="helpaaddbce2115bd8cd.png" border="0" />

###  Получение информации по всем таймерам в виде таблицы (команда info all (или ia))

<img src="https://s3.radikal.cloud/2024/12/22/iaaf6b9ca25510bd47.png" alt="iaaf6b9ca25510bd47.png" border="0" />

### Получение списка всех таймеров в виде списка (команда ls (или list))

<img src="https://s3.radikal.cloud/2024/12/22/ls1cf11d2df73769af.png" alt="ls1cf11d2df73769af.png" border="0" />

### Выход из программы (команда q (или quit))

<p>Когда же вы будете выходить из программы, при помощи команды, вам будет предложено:</p>

1) Вывести диаграмму, которая выводит соотношение времени, которое было насчитано таймерами
2) Сохранить эту выведенную диаграмму в виде png файла
3) Сохранить результат работы всех таймеров в виде таблицы в текстовый файл

<img src="https://s3.radikal.cloud/2024/12/22/q2bc48443f57f199d.png" alt="q2bc48443f57f199d.png" border="0" />

### 1) Пример диаграммы, которая выводится пользователю

<img src="https://s3.radikal.cloud/2024/12/22/diagramdaddd438afb2d854.png" alt="diagramdaddd438afb2d854.png" border="0" />

### 2) Пример уже сохраненной диаграммы в виде png файлa по пути, который стоит по умолчанию

<img src="https://s3.radikal.cloud/2024/12/22/diagram_pngf411c9d0da56b82c.png" alt="diagram_pngf411c9d0da56b82c.png" border="0" />

### 3) Пример результатов работы программы в текстовом файле

<img src="https://s3.radikal.cloud/2024/12/22/text7ea361facdb00c70.png" alt="text7ea361facdb00c70.png" border="0" />


## Разработчики

- [DarkPythons](https://github.com/DarkPythons)

## License
The Python-Timer project is distributed under the GPL-v3 license.
