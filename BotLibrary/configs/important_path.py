# BotLibrary/configs/important_path.py
# Хранилище всех важных путей


# Класс для хранения типов директорий
class TypeDirectory:
    # Типы сообщений и список директорий для создания
    private_msg = "Личные"
    group_msg = "Группы"
    msg_directories = [private_msg, group_msg]

    # Названия директорий для хранения аватаров
    user_avatar = "UserAvatar"
    chat_avatar = "ChatAvatar"
    channel_avatar = "ChannelAvatar"
    avatar_directories = [user_avatar, chat_avatar, channel_avatar]

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
    media_directories = [avatar, photo, video, videonote, 
                         gif, files, voice, youtube]


# Класс с важными путями и настройками
class ProjectPath:
    # Пути к файлам логирования
    logs = "BotLogs"
    log_start = f"{logs}/start.log"
    log_file = f"{logs}/bot.log"
    log_info = f"{logs}/info.log"
    log_error_file = f"{logs}/error.log"


    # Пути к хранилищу сообщений
    msg = f"{logs}/BotMessages"
    private_message = f"{msg}/{TypeDirectory.private_msg}"
    group_message = f"{msg}/{TypeDirectory.group_msg}"


    # Путь к хранилищу базы данных
    SQL = "MySQL"
    user_info_file = f"{SQL}/user_data.json"
    list_id = f"{SQL}/list_ids.json"


    # Пути к хранилищу медиа
    bot_files = "BotFiles"
    personal_media = f"BotLibrary/media"
    received_media = f"{bot_files}/MediaReceived"


    # Пути к папкам аватаров
    user_avatar = f"{bot_files}/{TypeDirectory.user_avatar}"
    chat_avatar = f"{bot_files}/{TypeDirectory.chat_avatar}"
    channel_avatar = f"{bot_files}/{TypeDirectory.channel_avatar}"


    # Путь к папкам хранения медиа
    console_app_avatar = f"{personal_media}/console_avatar.png"
    personal_avatar = f"{personal_media}/{TypeDirectory.avatar}"
    personal_photo = f"{personal_media}/{TypeDirectory.photo}"
    personal_video = f"{personal_media}/{TypeDirectory.video}"
    personal_videonote = f"{personal_media}/{TypeDirectory.videonote}"
    personal_gif = f"{personal_media}/{TypeDirectory.gif}"
    personal_document = f"{personal_media}/{TypeDirectory.files}"
    personal_voice = f"{personal_media}/{TypeDirectory.voice}"
    personal_youtube = f"{personal_media}/{TypeDirectory.youtube}"


    # Путь к папкам получения медиа
    received_avatar = f"{received_media}/{TypeDirectory.avatar}"
    received_photo = f"{received_media}/{TypeDirectory.photo}"
    received_video = f"{received_media}/{TypeDirectory.video}"
    received_videonote = f"{received_media}/{TypeDirectory.videonote}"
    received_gif = f"{received_media}/{TypeDirectory.gif}"
    received_document = f"{received_media}/{TypeDirectory.files}"
    received_voice = f"{received_media}/{TypeDirectory.voice}"
    received_youtube = f"{received_media}/{TypeDirectory.youtube}"
