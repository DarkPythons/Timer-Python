#!bin/bash

# Переменная, которая говорит, установлен ли poetry
poetry_shell_install=0

# Если команда для того чтобы узнать версию poetry сработает без ошибок
if poetry --version;
	then
		poetry_shell_install=1
		echo "У вас установлен poetry, начинаю загрузку окружения..."
else
	echo "К сожалению у вас не установлен poetry"
fi

if [ &poetry_shell_install -eq 0 ];
	then
		echo "Начинаю попытки установить poetry"
fi

# Если poetry не установлено
if [ &poetry_shell_install -eq 0 ];
	then
		# Если команда по установке poetry пройдет успешно
		if pip3 install poetry;
			then	
				poetry_shell_install=1
		fi
fi

# Если poetry до сих пор не установлено, вторая попытка
if [ &poetry_shell_install -eq 0 ];
	then
		# Если команда по установке poetry пройдет успешно
		if pip install poetry;
			then
				poetry_shell_install=1
		fi
fi

# Если poetry до сих пор не установлен
if [ &poetry_shell_install -eq 0 ];
	then
		# Если команда по установке poetry пройдет успешно
		if curl -sSL https://install.python-poetry.org | python3 -;
			then
				poetry_shell_install=1
		fi
fi

start_program=0

# Если poetry установлен
if [ &poetry_shell_install -eq 1 ];
	then
		echo "Poetry установлен, начинаю загрзку окружения. Ожидайте..."
		# Запуск загрузки окружения и библиотек
		poetry install
		# Изменение директории на директорию где лежит программа
		cd programm

		echo "Запуск программы."

		# Запуск приложения через окружение poetry
		if poetry run python main.py;
			then
				start_program=1
		fi
fi

if [ &start_program -eq 0 ];
	then
		echo "Запуск программы"
		if poetry run python main.py;
			then
				# Если программа была запущена через окружение без ошибок
				start_program=1
		fi
fi


if [ &start_program -eq 0 ];
	then
		echo "Запуск программы"
		if poetry run python3 main.py;
			then
				# Если программа была запущена через окружение без ошибок
				start_program=1
		fi
fi




