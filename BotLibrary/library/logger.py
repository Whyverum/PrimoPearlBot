# BotLibrary/library/logger.py
# Создание логгеров и подключение функций логирования в файлы

import sys
from loguru import logger
from config import ImportantPath, LogsSet
from ..analitics.message_to_file import write_message_to_file
from ..analitics.user_data_to_file import write_user_info_to_file

# Настройка экспорта модулей и логирования
__all__ = ("logger", "setup_logger", "cmd_logginger", "error_cmd_logginger",
           "logginger", "common_msg_logginger", )


# Создание обычного логгера + логгер в файл
async def setup_logger():
    logger.remove()  # Удаляем все логгеры

    # Пустой логгер для записи отступов в файл уровня TRACE
    logger.add(ImportantPath.log_file,
               rotation=LogsSet.max_size,
               format="\n\n\n",
               backtrace=True,
               diagnose=True,
               level="TRACE",
               filter=lambda record: record["level"].name == "TRACE")
    logger.trace("")

    # Логгер для вывода в консоль и файл с уровнем INFO
    logger.add(sys.stderr,
               colorize=True,
               format=LogsSet.info_text,
               level="INFO",
               filter=lambda record: record["level"].name == "INFO")
    logger.add(ImportantPath.log_file,
               rotation=LogsSet.max_size,
               format=LogsSet.info_text,
               backtrace=True,
               diagnose=True,
               level="INFO",
               filter=lambda record: record["level"].name == "INFO")

    # Логгер для вывода в консоль и файл с уровнем ERROR
    logger.add(sys.stderr,
               colorize=True,
               format=LogsSet.error_text,
               level="ERROR",
               filter=lambda record: record["level"].name == "ERROR")
    logger.add(ImportantPath.log_error_file,
               rotation=LogsSet.max_size,
               format=LogsSet.error_text,
               backtrace=True,
               diagnose=True,
               level="ERROR",
               filter=lambda record: record["level"].name == "ERROR")
    return f"Логгеры - подключены!"


# Запись сообщения в файл и информации о пользователи
async def logginger(message):
    write_user_info_to_file(message.from_user)
    await write_message_to_file(message)
    return f"Сообщение и информация о пользователи - успешно записаны!"


# Создание функции логирования на обычные сообщения
async def common_msg_logginger(message, name, message_type, log_type):
    # Проверка на наличие текста и его типа
    if message.text is None:
        logger.bind(log_type=log_type, user=f"@{message.from_user.username}").info(
            f"Получено сообщение из ({name}) : {message_type}")
    else:
        logger.bind(log_type=log_type, user=f"@{message.from_user.username}").info(
            f"Получено сообщение из ({name}) : {message.text}")
    return f"Логгер на обычный сообщения - успешно активирован"


# Специальный логгер для команд. Вывод в консоль, файл и запись информации о пользователи
async def cmd_logginger(message, log_type, text):
    await logginger(message)
    logger.bind(log_type=log_type, user=f"@{message.from_user.username}").info(text)
    return f"Логгер на команду - успешно активирован"


# Специальный логгер для ошибок с командами. Вывод в консоль, файл и запись информации о пользователи
async def error_cmd_logginger(message, log_type, e):
    text_error = f"Ошибка при использовании команды /{log_type.lower()}: {str(e)}\n"
    await logginger(message)
    logger.bind(log_type=log_type, user=f"@{message.from_user.username}").error(text_error)
    return text_error
