# BotLibrary/library/directory.py
# Небольшая библиотека для создания директорий

import os
from BotLibrary.configs import ProjectPath, TypeDirectory

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
    create_directories(ProjectPath.personal_media, TypeDirectory.media_directories)
    create_directories(ProjectPath.received_media, TypeDirectory.media_directories)
    create_directories(ProjectPath.bot_files, TypeDirectory.avatar_directories)
    create_directories(ProjectPath.msg, TypeDirectory.msg_directories)
