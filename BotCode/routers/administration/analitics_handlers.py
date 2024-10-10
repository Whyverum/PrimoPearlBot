# analitics_handlers.py

import datetime
import os

from aiogram import Router
from colorama import Fore

from BotCode import config


router = Router(name=__name__)


# Функция логирования запуска бота
async def write_bot_start_info():
    # with open(config.log_file_path, "a", encoding="utf-8") as file:
    # file.write(f"\nБот {config.bot_first_name} | @{config.bot_username}"
    # f" запущен в {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    # Форматирование информации о боте для вывода

    bot_str_start = f"Запуск бота начат в: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    bot_str_name = f"Основное имя: {config.bot_first_name}\n"
    bot_str_postname = f"Доп. имя: {config.bot_last_name}\n"
    bot_str_username = f"Юзернейм: @{config.bot_username}\n"
    bot_str_id = f"ID: {config.bot_id}\n"
    bot_str_language = f"Языковой код: {config.bot_language}\n"
    bot_str_group = f"Может ли вступать в группы?: {config.bot_can_join_groups}\n"
    bot_str_message = f"Чтение всех сообщений: {config.bot_can_read_all_group_messages}\n"

    print(Fore.BLUE + bot_str_name,
          Fore.BLUE + bot_str_postname,
          Fore.BLUE + bot_str_username,
          Fore.BLUE + bot_str_id,
          Fore.BLUE + bot_str_language,
          Fore.BLUE + bot_str_group,
          Fore.BLUE + bot_str_message)

    bot_info_str = (bot_str_start + bot_str_name + bot_str_postname + bot_str_username +
                    bot_str_id + bot_str_language + bot_str_group + bot_str_message)
    # Запись информации о боте в файл (перезапись файла)
    # with open(config.info_file_path, "w", encoding="utf-8") as file:
    # file.write(bot_info_str)  # Записываем новые данные


# Функция для записи сообщения в файл
async def write_message_to_file(message):
    # Проверка на тип файла
    if message.text:
        first_char = message.text.strip()[0]  # Извлекаем первый символ текста (убираем лишние пробелы)
        if first_char in config.prefix:
            file_type = "Command"
        else:
            file_type = "Text"
    elif message.photo:
        file_type = "Photo"
    elif message.sticker:
        file_type = "Sticker"
    elif message.animation:
        file_type = "GIF"
    elif message.voice:
        file_type = "Voice Message"
    elif message.video_note:
        file_type = "Video-Voice"
    elif message.video:
        file_type = "Video"
    elif message.audio:
        file_type = "Audio"
    elif message.document:
        file_type = "Document"
    elif message.contact:
        file_type = "Contact"
    elif message.location:
        file_type = "Location"
    elif message.venue:
        file_type = "Venue"
    elif message.boost_added:
        file_type = "GIVE BOOOOOST"
    else:
        file_type = "ERROR! UNKNOWN TYPE!"

    # Айди основных контактов
    chat_id = message.chat.id
    if chat_id in config.important_ids:
        name = config.important_ids[chat_id]
        file_path = f"BotFiles/BotMessages/Личные/{name}_messages.txt"
    elif chat_id <= 0:
        file_path = f"BotFiles/BotMessages/Личные/{message.from_user.username}_messages.txt"
    else:
        file_path = f"BotFiles/BotMessages/Личные/{chat_id}_messages.txt"

    # Директория для личных сообщений
    personal_messages_dir = os.path.join("BotFiles/BotMessages", "Личные")
    if not os.path.exists(personal_messages_dir):
        os.makedirs(personal_messages_dir)

    # Директория для групповых сообщений
    group_messages_dir = os.path.join("BotFiles/BotMessages", "Группы")
    if not os.path.exists(group_messages_dir):
        os.makedirs(group_messages_dir)

    # Проверяем существование файла
    if not os.path.exists(file_path):
        with open(file_path, "w", encoding="utf-8") as file:
            file.write("")

    # Запись информации в файл
    with open(file_path, "a", encoding="utf-8") as file:
        username = message.from_user.username if message.from_user.username else "No username"
        file.write(
            f"\n{datetime.datetime.now()} - {username} ({message.from_user.id}): {message.text} - Type: {file_type}  |  ChatID: {chat_id}\n\n")

    # Возвращения сообщения об успешной записи
    return "Сообщение пользователя успешно записано в файл."


# Функция на запись id пользователя в user_id_data.txt
async def write_user_info_to_file(user):
    # Проверка, существует ли директория, если нет, создать её
    directory = os.path.dirname(config.user_info_file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Проверка, был ли уже записан ID пользователя
    existing_user_ids = set()

    # Чтение данных из файла, если файл существует
    if os.path.exists(config.user_info_file_path):
        with open(config.user_info_file_path, "r", encoding="utf-8") as file:
            for line in file:
                if line.startswith("ID:"):
                    existing_user_ids.add(int(line.split(":")[1].strip()))

    # Проверка, был ли уже записан ID пользователя
    if user.id in existing_user_ids:
        return "ID пользователя уже присутствует в файле."

    # Запись информации о пользователе в файл
    with open(config.user_info_file_path, "a", encoding="utf-8") as file:
        file.write(f"Время знакомства: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        file.write(f"ID: {user.id}\n")
        file.write(f"Имя: {user.first_name}\n")
        if hasattr(user, 'last_name'):
            file.write(f"Фамилия: {user.last_name}\n")
        if hasattr(user, 'username'):
            file.write(f"Юзернейм: @{user.username}\n")
        if hasattr(user, 'language_code'):
            file.write(f"Язык: {user.language_code}\n")
        if hasattr(user, 'birthdate'):
            file.write(f"Дата рождения: {user.birthdate}\n")
        if hasattr(user, 'location'):
            file.write(f"Местоположение: {user.location}\n")
        if hasattr(user, 'contact_info'):
            file.write(f"Контактная информация: {user.contact_info}\n")
        if hasattr(user, 'contacts'):
            file.write("Контакты:\n")
            for contact in user.contacts:
                file.write(f"- {contact}\n")
        file.write("\n\n")

    # Возвращения сообщения об успешной записи
    return "Информация о пользователе успешно записана в файл."


# Функция объединения двух вышесказанных
async def loginger(message):
    await write_user_info_to_file(message.from_user)
    await write_message_to_file(message)
