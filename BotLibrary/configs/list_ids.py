# BotLibrary/configs/list_ids.py
# Получение id пользователей из базы данных

import os
import json
from loguru import logger

from .settings import default_encod
from .important_path import ProjectPath

# Настройка экспорта модулей и логирования
__all__ = ("load_ids_from_json", "save_ids_to_json", "DataID")
default_file = ProjectPath.list_id
log_type = "ListID"


# Чтение данных из файла JSON с обработкой ошибок
def load_ids_from_json(file=default_file, encoding=default_encod):
    try:
        # Проверка существования файла
        if not os.path.exists(file):
            # Если файл не существует, создаем его с пустым содержимым
            with open(file, "w", encoding=encoding) as f:
                json.dump({}, f, ensure_ascii=False, indent=4)

        # Чтение данных из файла
        with open(file, "r", encoding=encoding) as f:
            return json.load(f)

    except FileNotFoundError:
        (logger.bind(log_type=log_type, user="Файл id")
         .error(f"Файл {file} не найден!"))
        return {}

    except json.JSONDecodeError:
        (logger.bind(log_type=log_type, user="Декодирование id")
         .error(f"Ошибка декодирования JSON в файле {file}"))
        return {}

    except Exception as e:
        (logger.bind(log_type=log_type, user="Чтение id")
         .error(f"Произошла ошибка при чтении файла {file}: {e}"))
        return {}


# Запись данных в файл JSON с обработкой ошибок
def save_ids_to_json(file=default_file, encoding=default_encod, data=None):
    try:
        with open(file, "w", encoding=encoding) as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    except Exception as e:
        (logger.bind(log_type=log_type, user="Запись id")
         .error(f"Произошла ошибка при записи в файл {file}: {e}"))


# Класс для хранения данных из JSON
class DataID:
    # Получение информации из списка важных айди, забанненых айди и общих
    data_list_id = load_ids_from_json(ProjectPath.list_id)
    data_user_data = load_ids_from_json(ProjectPath.user_info_file)

    # Список забанненых пользователей
    ban_list = data_list_id.get("ban_list_ids", {})

    # Список важных айди
    admins = data_list_id.get("important_adm_ids", {})
    groups = data_list_id.get("important_groups_ids", {})
    users = data_list_id.get("important_users_list_ids", {})
    channels = data_list_id.get("important_channel_ids", {})
    important = {**groups, **admins, **users, **channels}
