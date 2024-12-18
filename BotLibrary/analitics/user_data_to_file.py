# BotLibrary/analitics/user_data_to_file.py
# Запись информации о пользователях в файл "user_data.db"   (Сделать счетчик пользователей)

import os
import json
import datetime
from config import ImportantPath, BotVariables

# Настройка экспорта модулей и логирования
__all__ = ("write_user_info_to_file", "format_user_record",)
log_type = "User_data_file"


# Функция записи информации в JSON-файл
def write_user_info_to_file(user):
    directory = os.path.dirname(ImportantPath.user_info_file)
    if not os.path.exists(directory):
        os.makedirs(directory)

    if os.path.exists(ImportantPath.user_info_file):
        with open(ImportantPath.user_info_file, "r", encoding=BotVariables.encoding) as file:
            try:
                user_data = json.load(file)
            except json.JSONDecodeError:
                user_data = {}
    else:
        user_data = {}

    user_record = format_user_record(user)
    user_data[str(user.id)] = user_record

    with open(ImportantPath.user_info_file, "w", encoding=BotVariables.encoding) as file:
        json.dump(user_data, file, ensure_ascii=False, indent=4)

    return f"Информация о пользователе успешно записана или обновлена."


# Функция форматирования вывода в JSON-файл
def format_user_record(user):
    first_name = getattr(user, 'first_name', '')  # Получаем имя
    last_name = getattr(user, 'last_name', '')    # Получаем фамилию или пустую строку

    return {
        "Время знакомства": datetime.datetime.now().strftime(BotVariables.time_format),
        "Имя": first_name,
        "Фамилия": last_name,
        "Юзернейм": f"@{getattr(user, 'username', 'Не указано')}",
        "Айди": user.id,
        "Ссылка": f"tg://user?id={user.id}",
        "Бот": getattr(user, 'is_bot', False),
        "Премиум": getattr(user, 'is_premium', False),
        "Язык": getattr(user, 'language_code', 'Не указано'),
    }

