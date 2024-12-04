# BotCode/settings/analitics/user_data_to_file.py

import os
import datetime
from ..configs.config import ImportantPath

# Работа с import *
__all__ = ("write_user_info_to_file",)
type_messages = "User_data_file"


# Функция на запись id пользователя в user_data.db
def write_user_info_to_file(user):
    # Проверка, существует ли директория, если нет, создать её
    directory = os.path.dirname(ImportantPath.user_info_file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Проверка, был ли уже записан ID пользователя
    existing_user_ids = set()

    # Чтение данных из файла, если файл существует
    if os.path.exists(ImportantPath.user_info_file_path):
        with open(ImportantPath.user_info_file_path, "r", encoding="utf-8") as file:
            for lines in file:
                if lines.startswith("ID:"):
                    existing_user_ids.add(int(lines.split(":")[1].strip()))

    # Проверка, был ли уже записан ID пользователя
    if user.id in existing_user_ids:
        return f"ID пользователя уже присутствует в файле."

    # Запись информации о пользователе в файл
    with open(ImportantPath.user_info_file_path, "a", encoding="utf-8") as file:
        # Запись времени, айди и имени пользователя
        file.write(f"Время знакомства: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        file.write(f"ID: {user.id}\n")
        file.write(f"Имя: {user.first_name}\n")

        # Проверка есть ли у пользователя фамилия
        if hasattr(user, 'last_name') and user.last_name:
            file.write(f"Фамилия: {user.last_name}\n")

        # Проверка есть ли у пользователя юзернейм
        if hasattr(user, 'username') and user.username:
            file.write(f"Юзернейм: @{user.username}\n")

        # Проверка есть ли у пользователя языковой код
        if hasattr(user, 'language_code') and user.language_code:
            file.write(f"Язык: {user.language_code}\n")

        # Проверка, является ли пользователь премиум
        if hasattr(user, 'is_premium') and user.is_premium is not None:
            file.write(f"Премиум: {user.is_premium}\n")

        # Проверка на добавление в меню вложений
        if hasattr(user, 'added_to_attachment_menu') and user.added_to_attachment_menu is not None:
            file.write(f"Добавлен в меню вложений: {user.added_to_attachment_menu}\n")

        # Проверка, может ли присоединяться к группам
        if hasattr(user, 'can_join_groups') and user.can_join_groups is not None:
            file.write(f"Может присоединяться к группам: {user.can_join_groups}\n")

        # Проверка, может ли читать все сообщения в группах
        if hasattr(user, 'can_read_all_group_messages') and user.can_read_all_group_messages is not None:
            file.write(f"Может читать все сообщения в группах: {user.can_read_all_group_messages}\n")

        # Проверка, поддерживает ли инлайн-запросы
        if hasattr(user, 'supports_inline_queries') and user.supports_inline_queries is not None:
            file.write(f"Поддерживает инлайн-запросы: {user.supports_inline_queries}\n")

        # Проверка, может ли подключаться к бизнесу
        if hasattr(user, 'can_connect_to_business') and user.can_connect_to_business is not None:
            file.write(f"Может подключаться к бизнесу: {user.can_connect_to_business}\n")

        # Проверка, имеет ли основной веб-приложение
        if hasattr(user, 'has_main_web_app') and user.has_main_web_app is not None:
            file.write(f"Имеет основной веб-приложение: {user.has_main_web_app}\n")

        # Проверка есть ли у пользователя дата рождения (если она предоставлена другим способом)
        if hasattr(user, 'birthdate') and user.birthdate:
            file.write(f"Дата рождения: {user.birthdate}\n")

        # Проверка есть ли у пользователя описание (about)
        if hasattr(user, 'about') and user.about:
            file.write(f"Описание: {user.about}\n")

        # Проверка есть ли у пользователя локация
        if hasattr(user, 'location') and user.location:
            file.write(f"Местоположение: {user.location}\n")

        # Проверка есть ли у пользователя контактная информация
        if hasattr(user, 'contact_info') and user.contact_info:
            file.write(f"Контактная информация: {user.contact_info}\n")

        # Проверка есть ли у пользователя канал, привязанный к профилю
        if hasattr(user, 'channel') and user.channel:
            file.write(f"Привязанный канал: {user.channel}\n")

        # Проверка есть ли у пользователя контакты
        if hasattr(user, 'contacts') and user.contacts:
            file.write(f"Контакты:\n")
            for contact in user.contacts:
                file.write(f"- {contact}\n")

        # Запись табуляции в файл
        file.write("\n\n")

    # Возвращение сообщения об успешной записи
    return f"Информация о пользователе успешно записана в файл."
