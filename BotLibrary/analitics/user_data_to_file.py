# BotLibrary/analitics/user_data_to_file.py
# Запись информации о пользователи в базу данных

import os
import json
import datetime

from aiogram.types import User, Birthdate
from ..configs import *
from ..library.time import TimeVariable

# Настройка экспорта модулей и логирования
__all__ = ("write_user_info_to_file", "format_user_record",)
log_type = "User_data_file"


# Функция записи информации в JSON-файл
def write_user_info_to_file(user: User):
    directory = os.path.dirname(ProjectPath.user_info_file)
    if not os.path.exists(directory):
        os.makedirs(directory)

    if os.path.exists(ProjectPath.user_info_file):
        with open(ProjectPath.user_info_file, "r", encoding=default_encod) as file:
            try:
                user_data = json.load(file)
            except json.JSONDecodeError:
                user_data = {}
    else:
        user_data = {}

    user_record = format_user_record(user)
    user_data[str(user.id)] = user_record

    with open(ProjectPath.user_info_file, "w", encoding=default_encod) as file:
        json.dump(user_data, file, ensure_ascii=False, indent=4)


# Функция форматирования вывода в JSON-файл
def format_user_record(user: User):
    first_name = getattr(user, 'first_name', '')  # Получаем имя
    last_name = getattr(user, 'last_name', '')    # Получаем фамилию или пустую строку

    # Получение даты рождения
    birthdate = getattr(user, 'birthdate', None)
    if isinstance(birthdate, Birthdate):
        birthdate_str = f"{birthdate.day:02d}.{birthdate.month:02d}.{birthdate.year or 'Не указано'}"
    else:
        birthdate_str = "Не указано"

    return {
        "Время знакомства": datetime.datetime.now().strftime(TimeVariable.format),
        "Имя": first_name,
        "Фамилия": last_name,
        "Юзернейм": f"@{getattr(user, 'username', 'Не указано')}",
        "Айди": user.id,
        "Ссылка": f"tg://user?id={user.id}",
        "Бот": getattr(user, 'is_bot', False),
        "Премиум": getattr(user, 'is_premium', False),
        "Язык": getattr(user, 'language_code', 'Не указано'),
        "Дата рождения": birthdate_str,  # Добавляем дату рождения
    }
