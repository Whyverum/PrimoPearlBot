# BotLibrary/library/directory.py
# Небольшая библиотека для создания директорий

import os
from config import ImportantPath, BotVariables

# Настройка экспорта модулей и логирования
__all__ = ("create_directories", "setup_directories", )
log_type = "Directory"


# Функция создания пустых директорий
def create_directories(base_directory, subdirectories):
    # Создание директорий и файлов в каждой из них
    for subdirectory in subdirectories:
        directory_path = os.path.join(base_directory, subdirectory)

        # Проверка, существует ли директория, если нет - создаём
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)


# Начальная установка пустых директорий
def setup_directories():
    create_directories(ImportantPath.bot_personal_media, BotVariables.bot_media_directories)
    create_directories(ImportantPath.bot_received_media, BotVariables.bot_media_directories)
    create_directories(ImportantPath.msg, BotVariables.bot_msg_directories)
    create_directories(ImportantPath.bot_files, BotVariables.bot_avatar_directories)
    return f"Пустые директории - успешно созданы!"
