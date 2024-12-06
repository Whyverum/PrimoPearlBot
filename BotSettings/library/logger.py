# BotSettings/library/logger.py
# Создание логгеров и подключение функций логирования в файлы

import sys
from loguru import logger

from ..analitics.message_to_file import write_message_to_file
from ..analitics.user_data_to_file import write_user_info_to_file
from BotSettings.library.config import (ImportantPath,
                                        logs_text,
                                        error_logs_text,
                                        max_size_log_file, )

# То что будет импортироваться при from logger import *
__all__ = ("sys", "logger", "setup_logger", "logginger", "cmd_logginger", "error_cmd_logginger",)
type_messages = "Logger"


# Создание обычного логгера + логгер в файл
def setup_logger():
    logger.remove()  # Удаляем все логгеры

    # Пустой логгер для записи отступов в файл
    logger.add(ImportantPath.log_file,
               rotation=max_size_log_file,
               format="\n\n\n",
               backtrace=True,
               diagnose=True, )
    logger.remove()

    # Логгер для записи в файл с ротацией и диагностической информацией
    logger.add(ImportantPath.log_file,
               rotation=max_size_log_file,
               format=logs_text,
               backtrace=True,
               diagnose=True,
               level="INFO",
               filter=lambda record: record["level"].name == "INFO", )

    # Логгер для записи в файл ошибок
    logger.add(ImportantPath.log_error_file,
               rotation=max_size_log_file,
               format=logs_text,
               backtrace=True,
               diagnose=True,
               level="ERROR",
               filter=lambda record: record["level"].name == "ERROR", )

    # Логгер для вывода в консоль
    logger.add(sys.stderr,
               colorize=True,
               format=logs_text,
               level="INFO",
               filter=lambda record: record["level"].name == "INFO",)

    # Логгер для вывода в консоль только для уровня ERROR
    logger.add(sys.stderr,
               colorize=True,
               format=error_logs_text,
               level="ERROR",
               filter=lambda record: record["level"].name == "ERROR",)

    return f"Логгеры подключены!"


# Запись сообщения в файл и информации о пользователи
async def logginger(message):
    write_user_info_to_file(message.from_user)
    await write_message_to_file(message)
    return f"Сообщение и информация о пользователи успешно записаны!"


# Специальный логгер для команд. Вывод в консоль, файл и запись информации о пользователи
async def cmd_logginger(message, command_text, text):
    await logginger(message)
    logger.bind(custom_variable=command_text, user_var=f"@{message.from_user.username}").info(text)
    return f"Логгер на команду успешно активирован"


# Специальный логгер для ошибок с командами. Вывод в консоль, файл и запись информации о пользователи
async def error_cmd_logginger(message, command_text, e):
    text_error = f"Ошибка при использовании команды /{command_text.lower()}: {str(e)}\n"
    await logginger(message)
    logger.bind(custom_variable=command_text, user_var=f"@{message.from_user.username}").error(text_error)
    return text_error
