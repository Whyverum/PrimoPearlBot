# download_handlers.py

import requests
import os
from loguru import logger
from aiogram import Router, F, types

from BotCode import config
from BotCode.routers.administration.analitics_handlers import loginger

router = Router(name=__name__)


# Функция для скачивания медиа отправленного в бота
@router.message(config.filtre)
async def handle_media(message: types.Message, bot):
    try:
        name = message.chat.id
        if name in config.important_ids:
            name = config.important_ids[name]
        await loginger(message)

        # Обработка видео и анимации
        if message.content_type in (types.ContentType.VIDEO, types.ContentType.ANIMATION):
            media = message.video if message.content_type == types.ContentType.VIDEO else message.animation
            file_name = media.file_name if media.file_name else f"{'video' if message.content_type == types.ContentType.VIDEO else 'gif'}_{media.file_id}"
            file_extension = media.mime_type.split('/')[-1]
            file_name_with_extension = f"{file_name}.{file_extension}"

            save_path = os.path.join(config.base_path,
                                     'Video' if message.content_type == types.ContentType.VIDEO else 'GIF')
            os.makedirs(save_path, exist_ok=True)  # Создаём директорию, если её нет

            file = await bot.get_file(media.file_id)
            logger.bind(custom_variable="Media", user_var=str(message.from_user.username)).info(
                f"Видеофайл из ({name}) успешно скачан!")
            await bot.download_file(file.file_path, os.path.join(save_path, file_name_with_extension))

        # Обработка документов
        elif message.content_type == types.ContentType.DOCUMENT:
            await loginger(message)

            file = await bot.get_file(message.document.file_id)
            file_name = message.document.file_name
            file_path = file.file_path

            save_path = os.path.join(config.base_path, 'Document')
            os.makedirs(save_path, exist_ok=True)  # Создаём директорию, если её нет

            logger.bind(custom_variable="Media", user_var=str(message.from_user.username)).info(
                f"Документ из ({name}) успешно скачан!")
            await bot.download_file(file_path, os.path.join(save_path, file_name))

        # Обработка голосовых сообщений
        elif message.content_type == types.ContentType.VOICE:
            await loginger(message)

            media = message.voice
            file_name = f"voice_{media.file_id}.ogg"  # Уникальное имя для голосовых сообщений

            save_path = os.path.join(config.base_path, 'Voice')
            os.makedirs(save_path, exist_ok=True)  # Создаём директорию, если её нет

            file = await bot.get_file(media.file_id)
            logger.bind(custom_variable="Media", user_var=str(message.from_user.username)).info(
                f"Голосовое сообщение из ({name}) успешно скачано!")
            await bot.download_file(file.file_path, os.path.join(save_path, file_name))

            # Обработка видео сообщений (video notes)
        elif message.content_type == types.ContentType.VIDEO_NOTE:
            await loginger(message)

            media = message.video_note
            file_name = f"video_note_{media.file_id}.mp4"

            save_path = os.path.join(config.base_path, 'VideoNote')
            os.makedirs(save_path, exist_ok=True)  # Создаём директорию, если её нет

            file = await bot.get_file(media.file_id)
            logger.bind(custom_variable="Media", user_var=str(message.from_user.username)).info(
                f"Видеосообщение из ({name}) успешно скачано!")
            await bot.download_file(file.file_path, os.path.join(save_path, file_name))


    except Exception as e:
        logger.bind(custom_variable="Media", user_var=str(message.from_user.username)).info("<red>МЕДИЯ ОШИБКА</red>!")
        print(f"Error downloading media: {e}")


# Функция для скачивания изображения с наивысшим разрешением
@router.message(F.photo)
async def download_image(message: types.Message, bot):
    try:
        name = message.chat.id
        if name in config.important_ids:
            name = config.important_ids[name]
        await loginger(message)

        # Создание папки, если она не существует
        if not os.path.exists(config.photo_path):
            os.makedirs(config.photo_path)

        # Получение информации о файле
        file_id = max(message.photo, key=lambda x: x.width * x.height).file_id
        file_info = await bot.get_file(file_id)
        file_url = f"https://api.telegram.org/file/bot{config.bot_token}/{file_info.file_path}"

        # Получение имени файла из URL
        file_name = os.path.join(config.photo_path, file_info.file_path.split("/")[-1])

        # Загрузка изображения
        response = requests.get(file_url)
        if response.status_code == 200:
            with open(file_name, "wb") as file:
                file.write(response.content)
            logger.bind(custom_variable="Media", user_var=str(message.from_user.username)).info(
                f"Фотография из ({name}) успешно скачана!")
            return f"Изображение с наивысшим разрешением успешно скачано: {file_name}"
        else:
            return f"Ошибка при загрузке изображения"
    except Exception as e:
        logger.bind(custom_variable="Media", user_var=str(message.from_user.username)).info(
            "<red>Фотография ОШИБКА</red>!")
        return f"Ошибка при скачивании изображения: {str(e)}"
