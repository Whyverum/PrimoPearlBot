# BotCode/settings/analitics/message_to_file.py     (сделать логирование на ошибки)

import os
import datetime
from .find_adm_list_id import find_chat_id
from .type_messages import types_message

# Работа с import *
__all__ = ("write_message_to_file",)
type_messages = "Message_file"


# Функция записи сообщений в отдельные файлы
async def write_message_to_file(message):
    # Создание переменных с информацией
    message_type = types_message(message)
    chat_id = find_chat_id(message)

    # Проверка на тип чата и запись в нужную директорию
    if message.chat.type == "private":
        file_path = f"BotFiles/BotMessages/Личные/{chat_id}.txt"
    else:
        file_path = f"BotFiles/BotMessages/Группы/{chat_id}.txt"

    # Проверка и создание директорий
    if not os.path.exists(os.path.dirname(file_path)):
        os.makedirs(os.path.dirname(file_path))

    # Запись информации в файл
    with open(file_path, "a", encoding="utf-8") as file:
        date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        username = message.from_user.username if message.from_user.username else "No username"

        # Проверка на наличие текста
        if message.text is None:
            file.write(
                f"{date} | {username} ({message.from_user.id}) | ChatID: {chat_id} "
                f"| Type: {message_type}\n\n")
        else:
            file.write(
                f"{date} | {username} ({message.from_user.id}) | ChatID: {chat_id} "
                f"| Текст: {message.text}\n\n")

    return f"Сообщение пользователя успешно записано в файл."
