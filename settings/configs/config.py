# BotCode/settings/configs/config.py

from ..configs.bot_secrets import (important_groups_ids,
                                   important_adm_ids,
                                   ban_list_ids,
                                   important_users_list_ids,)


# Шаблон логов для обычного логгера
logs_text = ("<green>{time:YYYY-MM-DD HH:mm:ss}</green> <red> | </red> "
             "<blue>PRIMO-{extra[custom_variable]}</blue> <red> | </red> "
             "<red>{extra[user_var]}  | </red> <level>{message}</level>")

# Максимальный размер лог-файла
max_size_log_file = "500 MB"

# Шаблон логов для логгера-ошибок
error_logs_text = ("<red>{time:YYYY-MM-DD HH:mm:ss}  |  "
                   "ERROR-{extra[custom_variable]}  | "
                   "{extra[user_var]} | </red><level>{message}</level>")


# Класс с параметрами бота
class BotEdit:
    name = "Имя бота"   # Описание имени бота
    description = "Привет, мое имя Бот Лейна! Рад с вами пообщаться!!!"  # Описание бота
    short_description = "ООп"   # Описание виджета бота
    prefixs = ('$', '!', '.', '%', '&', ':', '|', '+', '-', '/', '~', '?')  # Доступные префиксы бота


# Создание словарей с id пользователей
class ListId:
    # Получение списков из py
    ban_list_id = ban_list_ids
    adm_list_id = important_adm_ids

    important_users_list_id = important_users_list_ids
    groups_list_id = important_groups_ids

    # Создание единого словаря важных ID
    important_ids = important_users_list_ids.copy()
    important_ids.update(adm_list_id)
    important_ids.update(groups_list_id)


# Класс с важными переменными-пути
class ImportantPath:
    # Путь к аватару пользователя
    image_avatar_path = f"BotFiles/MediaPersonal/avatar.jpg"

    # Пути к важным файлам бота
    user_info_file_path = f"BotLogs/user_data.db"
    log_file_path = f"BotLogs/bot.log"
    log_start_file_path = f"BotLogs/bot_start.log"
    info_file_path = f"BotLogs/bot.info"
    secret_file_path = f"settings/configs/bot_secrets.py"

    # Пути к хранению медиа
    bot_personal_media = f"settings/MediaPersonal"
    bot_received_media = f"BotFiles/MediaReceived"
    user_avatar_path = f"BotFiles/UserAvatar"
    chat_avatar_path = f"BotFiles/ChatAvatar"

    # Названия директорий-хранилищ
    photo = "Photo"
    video = "Video"
    videonote = "VideoNote"
    gif = "GIF"
    document = "Document"
    voice = "Voice"
    youtube = "YouTube"

    # Названия директорий-хранилищ для закачки
    photo_directory = f"{bot_received_media}/{photo}/"
    video_directory = f"{bot_received_media}/{video}/"
    videonote_directory = f"{bot_received_media}/{videonote}/"
    gif_directory = f"{bot_received_media}{gif}/"
    document_directory = f"{bot_received_media}/{document}/"
    voice_directory = f"{bot_received_media}/{voice}/"
    youtube_directory = f"{bot_received_media}/{youtube}/"
