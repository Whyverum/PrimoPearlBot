# BotSettings/configs/config.py
# Список практически всех переменных проекта

from ..configs.bot_secrets import (important_groups_ids,
                                   important_adm_ids,
                                   ban_list_ids,
                                   important_users_list_ids, )

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
    name = "Первородная Жемчужина"  # Описание имени бота
    description = ("Привет, мое имя - Эми! Я буду рада, вам помочь "
                   "посетить другие миры! Вместе!")  # Описание бота
    short_description = "Привет, это описание! Как дела?"  # Описание виджета бота
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
    # Путь к файлу с важной информацией (токенами)
    secret_file_path = f"settings/configs/bot_secrets.py"

    # Пути к файлам логирования
    log_start_path = f"BotLogs/bot_start.log"
    log_file_path = f"BotLogs/bot.log"
    log_error_file_path = f"BotLogs/bot_error.log"
    log_info_path = f"BotLogs/bot_info.log"

    # Пути к хранению сообщений
    private_message = f"BotLogs/BotMessages/Личные"
    group_message = f"BotLogs/BotMessages/Группы"

    # Путь к хранилищу базы данных
    user_info_file_path = f"BotLogs/user_data.db"

    # Пути к хранению медиа
    bot_personal_media = f"BotSettings/MediaPersonal"
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
    gif_directory = f"{bot_received_media}/{gif}/"
    document_directory = f"{bot_received_media}/{document}/"
    voice_directory = f"{bot_received_media}/{voice}/"
    youtube_directory = f"{bot_received_media}/{youtube}/"
