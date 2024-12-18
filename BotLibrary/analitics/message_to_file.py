# BotLibrary/analitics/message_to_file.py
# Запись сообщений в файлы в зависимости от группы и личных сообщений

import os
from loguru import logger
from datetime import datetime

from config import BotVariables
from .type_messages import *
from .find_ids import find_chat_id

# Настройка экспорта модулей и логирования
__all__ = ("write_message_to_file",)
log_type = "Message_file"


# Функция записи сообщений в отдельные файлы
async def write_message_to_file(message):
    try:
        # Создание переменных с информацией
        message_type = types_message(message)
        chat_id = find_chat_id(message)
        file_path = types_chat(message)

        # Переменные для логов сообщений
        date = datetime.now().strftime(BotVariables.time_format)
        username = message.from_user.username if message.from_user.username else "No username"
        log_shablon = f"{date} | @{username} ({message.from_user.id}) |"

        # Проверка и создание директорий
        if not os.path.exists(os.path.dirname(file_path)):
            os.makedirs(os.path.dirname(file_path))

        # Запись информации в файл
        with open(file_path, "a", encoding=BotVariables.encoding) as file:
            # Проверка на наличие текста
            if message.text is None:
                file.write(f"{log_shablon} Тип: {message_type}\n\n")
            else:
                file.write(f"{log_shablon} ChatID: {chat_id} | Текст: {message.text}\n\n")

        return f"Сообщение пользователя успешно записано в файл."

    # Проверка на ошибку и ее логирование
    except Exception as e:
        text_error = f"Ошибка в сохранении сообщения в файл: {str(e)}"
        logger.bind(custom_variable=log_type, user_var=f"@{message.from_user.username}").error(text_error)
        return text_error
