import datetime, os, requests
from BotCode import config
from config import settings
from aiogram import types
from pytube import YouTube

# Функция логирования запуска бота
async def write_bot_start_info(file_path, bot_first_name, bot_username):
    with open(file_path, "a", encoding="utf-8") as file:
        file.write(f"\nБот {bot_first_name} | @{bot_username} запущен в {datetime.datetime.now()}\n")


# Функция для записи информации о боте в файл
async def write_bot_info_to_file(bot_info_str):
    # Запись новых данных в файл
    with open(config.info_file_path, "w", encoding="utf-8") as file:
        file.write(bot_info_str)  # Записываем новые данные


# Функция для получения информации о боте
async def get_bot_info(bot):
    bot_info = await bot.get_me()
    bot_id = bot_info.id
    bot_first_name = bot_info.first_name
    bot_last_name = bot_info.last_name
    bot_username = bot_info.username
    bot_language_code = bot_info.language_code
    bot_can_join_groups = bot_info.can_join_groups
    bot_can_read_all_group_messages = bot_info.can_read_all_group_messages

    # Форматирование информации о боте для вывода
    bot_info_str = f"Запуск бота начат в: {datetime.datetime.now()}\n"
    bot_info_str += f"\nОсновное имя: {bot_first_name}\n"
    bot_info_str += f"Доп. имя: {bot_last_name}\n"
    bot_info_str += f"Юзернейм: @{bot_username}\n"
    bot_info_str += f"ID: {bot_id}\n"
    bot_info_str += f"Языковой код: {bot_language_code}\n"
    bot_info_str += f"Может ли вступать в группы?: {bot_can_join_groups}\n"
    bot_info_str += f"Чтение всех сообщений: {bot_can_read_all_group_messages}\n"

    # Запись информации о боте в файл (перезапись файла)
    await write_bot_info_to_file(bot_info_str)

    return bot_info_str, bot_first_name, bot_username


# Функция для записи сообщения в файл
async def write_message_to_file(message):
    current_datetime = datetime.datetime.now()
    file_type = ""

    if message.content_type == types.ContentType.TEXT:
        first_char = message.text.strip()[0]  # Извлекаем первый символ текста (убираем лишние пробелы)
        if first_char in config.prefixs:
            file_type = "Command"
        else:
            file_type = "Text"
    elif message.content_type == types.ContentType.PHOTO:
        file_type = "Photo"
    elif message.photo:
        file_type = "Sticker"
    elif message.animation:
        file_type = "GIF"
    elif message.content_type == types.ContentType.VOICE:
        file_type = "Voice Message"
    elif message.content_type == types.ContentType.VIDEO_NOTE:
        file_type = "Video-Voice"
    elif message.content_type == types.ContentType.VIDEO:
        file_type = "Video"
    elif message.content_type == types.ContentType.AUDIO:
        file_type = "Audio"
    elif message.content_type == types.ContentType.DOCUMENT:
        file_type = "Document"
    elif message.content_type == types.ContentType.CONTACT:
        file_type = "Contact"
    elif message.content_type == types.ContentType.LOCATION:
        file_type = "Location"
    elif message.content_type == types.ContentType.VENUE:
        file_type = "Venue"
    elif message.content_type == types.ContentType.MESSAGE_AUTO_DELETE_TIMER_CHANGED:
        file_type = "Auto-Delete Timer Changed"
    elif message.content_type == types.ContentType.BOOST_ADDED:
        file_type = "GIVE BOOOOOST"
    else:
        file_type = "ERROR! UNKNOWN TYPE!"

    chat_id = message.chat.id
    if chat_id == 6751720805:
        file_path = f"BotMessages/Лейн_messages.txt"
    elif chat_id == 1570652377:
        file_path = f"BotMessages/Рикси_messages.txt"
    elif chat_id == 7051557370:
        file_path = f"BotMessages/Риша_messages.txt"
    elif chat_id == 1398573474:
        file_path = f"BotMessages/Финаки_messages.txt"

    elif chat_id == -1002247934490:
        file_path = f"BotMessages/Сплетни_лавочек_messages.txt"
    elif chat_id == -1002124483077:
        file_path = f"BotMessages/Труба_Сквад_messages.txt"
    elif chat_id == -1002123850090:
        file_path = f"BotMessages/Тест_Чат_messages.txt"
    else:
        file_path = f"BotMessages/{chat_id}_messages.txt"

    # Проверяем существование файла
    if not os.path.exists(file_path):
        with open(file_path, "w", encoding="utf-8") as file:
            file.write("")

    with open(file_path, "a", encoding="utf-8") as file:
        username = message.from_user.username if message.from_user.username else "No username"
        file.write(
            f"\n{current_datetime} - {username} ({message.from_user.id}): {message.text} - Type: {file_type}  |  ChatID: {chat_id}\n\n")


# Функция на запись id пользователя в user_id_data.txt
async def write_user_info_to_file(user):

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
        file.write(f"Время знакомства: {datetime.datetime.now()}\n")
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

    return "Информация о пользователе успешно записана в файл."


# Функция для скачивания изображения с наивысшим разрешением
async def download_image(photo_sizes, bot, folder_path=config.photo_path):
    try:
        # Создание папки, если она не существует
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # Находим фото с самым большим размером
        highest_resolution_photo = max(photo_sizes, key=lambda x: x.width * x.height)

        # Получение информации о файле
        file_id = highest_resolution_photo.file_id
        file_info = await bot.get_file(file_id)
        file_url = f"https://api.telegram.org/file/bot{settings.bot_token}/{file_info.file_path}"

        # Получение имени файла из URL
        file_name = os.path.join(folder_path, file_info.file_path.split("/")[-1])

        # Загрузка изображения
        response = requests.get(file_url)
        if response.status_code == 200:
            with open(file_name, "wb") as file:
                file.write(response.content)
            return f"Изображение с наивысшим разрешением успешно скачано: {file_name}"
        else:
            return "Ошибка при загрузке изображения"
    except Exception as e:
        return f"Ошибка при скачивании изображения: {str(e)}"



async def download_youtube(update, context):
    if len(context.args) != 1:
        update.message.reply_text("Используйте: /download <ссылка на видео>")
        return

    url = context.args[0]

    try:
        yt = YouTube(url)
        видео = yt.streams.get_highest_resolution()
        файл_пути = видео.download()

        # Отправка видео пользователю
        with open(файл_пути, 'rb') as видео_файл:
            update.message.reply_video(видео_файл)

        # Удаление файла после отправки
        os.remove(файл_пути)

    except Exception as e:
        update.message.reply_text(f"Произошла ошибка: {e}")
