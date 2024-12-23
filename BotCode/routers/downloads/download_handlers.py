# BotCode/BotLibrary/analitics/log_type.py
# Закачка всех полученных медиа в бота (в разработке + сделать логирование!!!)

import os
import requests
from aiogram import Router, types

from BotLibrary import *
from .download_avatar_all import download_avatar

# Создание роутера и настройка экспорта модулей
__all__ = ("router", "handle_media",)
router = Router(name="download_media_router")
log_type = "Media"


# Функция для скачивания медиа отправленного в бота
@router.message(F_Media)
async def handle_media(message: types.Message):
    try:
        await download_avatar(message)
        name = find_imp_id(message.from_user.id)
        await logginger(message)
        file_id = None

        # Определяем тип контента и соответствующие параметры
        if message.content_type in (types.ContentType.VIDEO, types.ContentType.ANIMATION):
            media = message.video if message.content_type == types.ContentType.VIDEO else message.animation
            file_extension = media.mime_type.split('/')[-1]  # Получаем расширение файла (например, "mp4" или "gif")
            file_name = f"{media.file_id}.{file_extension}"  # Используем file_id и расширение для имени
            save_dir = ProjectPath.received_video if message.content_type == types.ContentType.VIDEO \
                else ProjectPath.received_gif

        elif message.content_type == types.ContentType.PHOTO:
            media = message.photo
            # Получение file_id для самого качественного фото
            file_id = max(message.photo, key=lambda x: x.width * x.height).file_id
            file_info = await bot.get_file(file_id)
            # Имя файла будет взято из file_path, который содержит оригинальное имя файла
            file_name = file_info.file_path.split('/')[-1]  # Используем имя файла из пути
            save_dir = ProjectPath.received_photo

        elif message.content_type == types.ContentType.VOICE:
            media = message.voice
            file_name = f"{media.file_id}.ogg"  # Для голосовых сообщений используем file_id и расширение .ogg
            save_dir = ProjectPath.received_voice

        elif message.content_type == types.ContentType.VIDEO_NOTE:
            media = message.video_note
            file_name = f"{media.file_id}.mp4"  # Для видеосообщений используем file_id и расширение .mp4
            save_dir = ProjectPath.received_videonote

        elif message.content_type == types.ContentType.DOCUMENT:
            media = message.document
            file_name = media.file_name  # Для видеосообщений используем file_id и расширение .mp4
            save_dir = ProjectPath.received_document

        else:
            (logger.bind(log_type=log_type, user=message.from_user.username)
             .error(f"Неизвестный тип контента: {message.content_type}"))
            raise ValueError()

        # Убедимся, что директория существует
        os.makedirs(save_dir, exist_ok=True)

        # Если это фото, file_id был определен внутри блока обработки фото
        if file_id is not None:
            file_info = await bot.get_file(file_id)
        else:
            file_info = await bot.get_file(media.file_id)

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
        logger.bind(log_type=log_type, user=f"@{message.from_user.username}").info(
            f"Файл из ({name}) успешно скачан! Сохранён как: {save_path}")

    except ValueError as ve:
        # Обработка ошибок типа контента
        (logger.bind(log_type=log_type, user=f"@{message.from_user.username}")
         .error(f"ОШИБКА: {str(ve)}"))

    except Exception as e:
        # Логирование общих ошибок
        (logger.bind(log_type=log_type, user=f"@{message.from_user.username}")
         .error(f"МЕДИЯ ОШИБКА: {str(e)}"))
