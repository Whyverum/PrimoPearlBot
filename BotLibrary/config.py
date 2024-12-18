# BotLibrary/configs/config.py
# Список практически всех переменных проекта

from os import getenv
from dotenv import load_dotenv
from MySQL.list_ids import *


# Настройка экспорта модулей и логирования
__all__ = ("LogsSet", "BotEdit", "ListId", "ImportantPath", "BotVariables",
           "bot_token", "api_key", "web_api_key", )
log_type = "Config"


# Загружаем переменные из файла .env
load_dotenv()
bot_token = getenv("main_bot_token")
api_key = getenv("APIKey")
web_api_key = getenv("WebAPIKey")
important_id = getenv("important_id")
secret = getenv("secret")


# Класс для параметров логгера
class LogsSet:
    # Максимальный размер лог-файла
    max_size = "500 MB"

    # Шаблон логов для обычного логгера
    info_text = ("<green>{time:YYYY-MM-DD HH:mm:ss}</green> <red> | </red> "
                "<blue>PRIMO-{extra[log_type]}</blue> <red> | </red> "
                "<red>{extra[user]}  | </red> <level>{message}</level>")

    # Шаблон логов для логгера-ошибок
    error_text = ("<level>{time:YYYY-MM-DD HH:mm:ss}  |  ERROR-{extra[log_type]}  | "
                  "{extra[user]} | {message}</level>")


# Прочие переменные для проекта
class BotVariables:
    # Основные настройки бота
    encoding = "utf-8"
    time_format = "%Y-%m-%d %H:%M:%S"
    language = "Python-Aiogram"
    time_zone = "Asia/Novosibirsk"

    # Типы сообщений и список директорий для создания
    private_msg = "Личные"
    group_msg = "Группы"
    bot_msg_directories = [private_msg, group_msg,]

    # Названия директорий для хранения аватаров
    user_avatar = "UserAvatar"
    chat_avatar = "ChatAvatar"
    channel_avatar = "ChannelAvatar"
    bot_avatar_directories = [user_avatar, chat_avatar, channel_avatar,]

    # Названия директорий-хранилищ
    avatar = "Avatar"
    photo = "Photo"
    video = "Video"
    videonote = "VideoNote"
    gif = "GIF"
    files = "Document"
    voice = "Voice"
    youtube = "YouTube"

    # Список директорий для создания
    bot_media_directories = [
        avatar, photo, video, videonote, gif, files, voice, youtube,
    ]


# Класс с параметрами бота
class BotEdit:
    name = "Первородная Жемчужина"  # Описание имени бота
    description = ("Привет, мое имя - Эми! Я буду рада, вам помочь "
                   "посетить другие миры! Вместе!")  # Описание бота
    short_description = "Привет, это описание! Как дела?"  # Описание виджета бота
    prefixs = ('$', '!', '.', '%', '&', ':', '|', '+', '-', '/', '~', '?')  # Доступные префиксы бота


# Создание списков с ids пользователей
class ListId:
    # Получение списков из базы данных
    ban_list_id = ban_list_ids

    adm_list_id = important_adm_ids
    important_users_list_id = important_users_list_ids
    groups_list_id = important_groups_ids
    channel_list_id = important_channel_ids

    # Создание единого словаря важных ID с использованием оператора |
    important_ids = (important_adm_ids | important_users_list_ids |
                     important_groups_ids | important_channel_ids)


# Класс с важными переменными-пути
class ImportantPath:
    # Путь к аватарам проекта
    bot_avatar = f"BotLibrary/MediaPersonal/bot_avatar.png"
    console_app_avatar = f"BotLibrary/MediaPersonal/console_avatar.png"

    # Пути к файлам логирования
    log_start = f"BotLogs/bot_start.log"
    log_file = f"BotLogs/bot.log"
    log_info = f"BotLogs/bot_info.log"
    log_error_file = f"BotLogs/bot_error.log"

    # Пути к хранению сообщений
    msg = f"BotLogs/BotMessages"
    private_message = f"{msg}/{BotVariables.private_msg}"
    group_message = f"{msg}/{BotVariables.group_msg}"

    # Путь к хранилищу базы данных
    user_info_file = f"MySQL/user_data.json"

    # Пути к хранению медиа
    bot_files = f"BotFiles"
    bot_personal_media = f"BotLibrary/media"
    bot_received_media = f"BotFiles/MediaReceived"
    user_avatar = f"{bot_files}/{BotVariables.user_avatar}"
    chat_avatar = f"{bot_files}/{BotVariables.chat_avatar}"
    channel_avatar = f"{bot_files}/{BotVariables.channel_avatar}"


    # Названия директорий-хранилищ для медиа
    bot_avatar_directory = f"{bot_personal_media}/{BotVariables.avatar}/"
    bot_photo_directory = f"{bot_personal_media}/{BotVariables.photo}/"
    bot_video_directory = f"{bot_personal_media}/{BotVariables.video}/"
    bot_videonote_directory = f"{bot_personal_media}/{BotVariables.videonote}/"
    bot_gif_directory = f"{bot_personal_media}/{BotVariables.gif}/"
    bot_document_directory = f"{bot_personal_media}/{BotVariables.files}/"
    bot_voice_directory = f"{bot_personal_media}/{BotVariables.voice}/"
    bot_youtube_directory = f"{bot_personal_media}/{BotVariables.youtube}/"

    # Названия директорий-хранилищ для закачки
    avatar_directory = f"{bot_received_media}/{BotVariables.avatar}/"
    photo_directory = f"{bot_received_media}/{BotVariables.photo}/"
    video_directory = f"{bot_received_media}/{BotVariables.video}/"
    videonote_directory = f"{bot_received_media}/{BotVariables.videonote}/"
    gif_directory = f"{bot_received_media}/{BotVariables.gif}/"
    document_directory = f"{bot_received_media}/{BotVariables.files}/"
    voice_directory = f"{bot_received_media}/{BotVariables.voice}/"
    youtube_directory = f"{bot_received_media}/{BotVariables.youtube}/"
