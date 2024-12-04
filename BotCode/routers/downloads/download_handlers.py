# BotCode/settings/analitics/type_messages.py

import os
import requests
from aiogram import Router, types

from settings import *
from .download_user_avatar import download_user_photos
# from settings.library.bots import F_Media

# Создание роутера "download_media_router"
router = Router(name="download_media_router")
type_messages = "Media"


# Функция для скачивания медиа отправленного в бота
@router.message(F_Media)
async def handle_media(message: types.Message):
    try:
        await download_user_photos(message)
        name = find_chat_id(message)
        await logginger(message)

        # Определяем тип контента и соответствующие параметры
        if message.content_type in (types.ContentType.VIDEO, types.ContentType.ANIMATION):
            media = message.video if message.content_type == types.ContentType.VIDEO else message.animation
            file_extension = media.mime_type.split('/')[-1]  # Получаем расширение файла (например, "mp4" или "gif")
            file_name = f"{media.file_id}.{file_extension}"  # Используем file_id и расширение для имени
            save_dir = ImportantPath.video_directory if message.content_type == types.ContentType.VIDEO \
                else ImportantPath.gif_directory

        elif message.content_type == types.ContentType.PHOTO:
            media = message.photo
            # Получение информации о файле
            file_id = max(message.photo, key=lambda x: x.width * x.height).file_id
            file_info = await bot.get_file(file_id)
            # Имя файла будет взято из file_path, который содержит оригинальное имя файла
            file_name = file_info.file_path.split('/')[-1]  # Используем имя файла из пути
            save_dir = ImportantPath.photo_directory

        elif message.content_type == types.ContentType.VOICE:
            media = message.voice
            file_name = f"{media.file_id}.ogg"  # Для голосовых сообщений используем file_id и расширение .ogg
            save_dir = ImportantPath.voice_directory

        elif message.content_type == types.ContentType.VIDEO_NOTE:
            media = message.video_note
            file_name = f"{media.file_id}.mp4"  # Для видеосообщений используем file_id и расширение .mp4
            save_dir = ImportantPath.videonote_directory

        else:
            raise ValueError(f"Неизвестный тип контента: {message.content_type}")

        # Убедимся, что директория существует
        os.makedirs(save_dir, exist_ok=True)

        # Скачиваем файл
        file_info = await bot.get_file(media.file_id if message.content_type != types.ContentType.PHOTO else file_id)
        save_path = os.path.join(save_dir, file_name)

        # Загружаем медиафайл
        if message.content_type == types.ContentType.PHOTO:
            # Для фото скачиваем отдельно
            file_url = f"https://api.telegram.org/file/bot{bot_token}/{file_info.file_path}"
            response = requests.get(file_url)
            if response.status_code == 200:
                with open(save_path, "wb") as file:
                    file.write(response.content)
        else:
            await bot.download_file(file_info.file_path, save_path)

        # Логирование успешного скачивания
        logger.bind(custom_variable=type_messages, user_var=str(message.from_user.username)).info(
            f"Файл из ({name}) успешно скачан! Сохранён как: {save_path}"
        )

    except ValueError as ve:
        # Обработка ошибок типа контента
        (logger.bind(custom_variable=type_messages, user_var=str(message.from_user.username))
         .info(f"{TextDecorator.RED}ОШИБКА: {str(ve)}{TextDecorator.RESET_DECORATOR}"))
        print(f"Ошибка обработки медиа: {ve}")

    except Exception as e:
        # Логирование общих ошибок
        (logger.bind(custom_variable=type_messages, user_var=str(message.from_user.username))
         .info(f"{TextDecorator.RED}МЕДИЯ ОШИБКА{TextDecorator.RESET_DECORATOR}!"))
        print(f"Ошибка скачивания медиа: {e}")
