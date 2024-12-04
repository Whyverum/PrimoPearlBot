# BotCode/settings/library/logger.py

import sys
from loguru import logger

from ..analitics.message_to_file import write_message_to_file
from ..analitics.user_data_to_file import write_user_info_to_file
from ..configs.config import (ImportantPath,
                              logs_text,
                              error_logs_text,
                              max_size_log_file,)

# То что будет импортироваться при from logger import *
__all__ = ("sys", "logger", "setup_logger", "logginger")
type_messages = "Logger"


# Создание обычного логгера + логгер в файл
def setup_logger():
    logger.remove()  # Удаляем все логгеры

    # Логгер для записи в файл с ротацией и диагностической информацией
    logger.add(ImportantPath.log_file_path,
               rotation=max_size_log_file,
               backtrace=True,
               diagnose=True)

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
