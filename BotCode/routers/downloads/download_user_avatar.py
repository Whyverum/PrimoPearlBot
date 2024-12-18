# BotCode/routers/downloads/download_user_avatar.py
# Закачка всех аватаров пользователей

import os
from aiogram import Router, types
from aiogram.types import UserProfilePhotos
from BotLibrary import *


# Создание роутера и настройка экспорта модулей
__all__ = ("router", "download_user_photos",)
router = Router(name="avatar_router")
log_type = "AvatarUser"


# Функция закачки аватарок пользователя
async def download_user_photos(message: types.Message):
    try:
        # Получение ID пользователя
        user_id = message.from_user.id

        # Получение аватарок пользователя
        user_profile_photos: UserProfilePhotos = await bot.get_user_profile_photos(user_id)

        # Проверка на наличие в списке "важных" пользователей
        user_id = find_people_id(user_id)

        # Проверка наличия фотографий
        if user_profile_photos.total_count == 0:
            return f"У пользователя {user_id} нет аватарок."

        # Объявление пути и создание директории
        user_directory = f'{ImportantPath.user_avatar}/{user_id}'
        os.makedirs(user_directory, exist_ok=True)

        # Закачка аватарок пользователя
        for index, photo_set in enumerate(user_profile_photos.photos):
            for photo_index, photo in enumerate(photo_set):
                file = await bot.get_file(photo.file_id)
                # Путь для сохранения фотографии с началом индекса с 1
                file_path = f'{user_directory}/{user_id}_{index + 1}.png'
                await bot.download_file(file.file_path, file_path)
        return f"Аватарки пользователя {user_id} успешно закачаны!"

    except Exception as e:
        text_error = f"Ошибка при закачке аватарок пользователя: {str(e)}"
        logger.bind(log_type=log_type, user=f"@{message.from_user.username}").error(text_error)
        return text_error
