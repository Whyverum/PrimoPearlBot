# BotSettings/analitics/user_data_to_file.py
# Запись информации о пользователях в файл "user_data.db"   (Сделать счетчик пользователей)

import os
import datetime
from BotSettings.library.config import ImportantPath

# Настройка экспорта модулей
__all__ = ("write_user_info_to_file",)
type_messages = "User_data_file"


# Функция записи информации о пользователи в файл
def write_user_info_to_file(user):
    # Проверка, существует ли директория, если нет, создать её
    directory = os.path.dirname(ImportantPath.user_info_file)
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Считываем все существующие записи
    existing_records = {}
    if os.path.exists(ImportantPath.user_info_file):
        with open(ImportantPath.user_info_file, "r", encoding="utf-8") as file:
            record = []
            current_id = None
            for line in file:
                if line.startswith("Время знакомства:"):
                    if record and current_id:
                        existing_records[current_id] = record
                    record = [line]
                    current_id = None
                else:
                    record.append(line)
                    if line.startswith(" Айди:"):
                        current_id = int(line.split(":")[1].strip())  # Сохраняем ID пользователя
            if record and current_id:
                existing_records[current_id] = record  # Добавляем последнюю запись

    # Форматируем новую запись
    formatted_record = _format_user_record(user)
    user_id = user.id

    # Обновляем или добавляем запись
    existing_records[user_id] = formatted_record

    # Перезаписываем файл с обновлёнными записями
    with open(ImportantPath.user_info_file, "w", encoding="utf-8") as file:
        for record in existing_records.values():
            file.writelines(record)

    return f"Информация о пользователе успешно записана или обновлена."


# Вспомогательная функция перезаписи данных
def _format_user_record(user):
    # Форматируем данные пользователя для записи в файл
    first_name = getattr(user, 'first_name', '')
    last_name = getattr(user, 'last_name', '')
    full_name = first_name if last_name is None else f"{first_name} {last_name}"
    username = getattr(user, 'username', 'Не указано')
    is_bot = getattr(user, 'is_bot', 'False')
    is_premium = getattr(user, 'is_premium', False)  # Если None, будет False
    language_code = getattr(user, 'language_code', 'Не указано')

    # Создаем строку для записи
    record = [
        f"Время знакомства: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n",
        f" Имя: {full_name}\n",
        f" Юзернейм: @{username}\n",
        f" Айди: {user.id}\n",
        f" Ссылка: tg://user?id={user.id}\n",
        f" Бот: {is_bot}\n",
        f" Премиум: {is_premium}\n",
        f" Язык: {language_code}\n\n"
    ]
    return record
