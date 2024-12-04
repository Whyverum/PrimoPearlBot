# BotCode/routers/downloads/download_chat_avatar.py

import os
import requests
from aiogram.types import Chat
from settings import *


# Функция закачки аватарок чатов
async def download_chat_avatar(chat: Chat):
    try:
        if chat.type == "group" or chat.type == "supergroup":
            # Получаем информацию о фотографии аватара чата
            chat_id = chat.id
            file_info = await bot.get_chat_photo(chat_id)

            if not file_info:
                print(f"Чат с ID {chat_id} не имеет аватара.")
                return

            # Получаем file_id для фото
            file_id = file_info.file_id
            file_info = await bot.get_file(file_id)

            # Строим URL для скачивания файла
            file_url = f"https://api.telegram.org/file/bot{bot.token}/{file_info.file_path}"

            # Формируем имя и путь для сохранения фото
            save_dir = f"{ImportantPath.chat_avatar_path}/{chat_id}"
            os.makedirs(save_dir, exist_ok=True)
            file_name = file_info.file_path.split("/")[-1]  # Имя файла (например, "abc.jpg")
            save_path = os.path.join(save_dir, file_name)

            # Скачиваем аватар
            response = requests.get(file_url)
            if response.status_code == 200:
                with open(save_path, "wb") as file:
                    file.write(response.content)
                print(f"Фото аватара чата с ID {chat_id} успешно скачано и сохранено как {save_path}")
            else:
                print(f"Не удалось скачать фото аватара чата с ID {chat_id}. Статус: {response.status_code}")

    except Exception as e:
        print(f"Ошибка при скачивании фото аватара чата с ID {chat.id}: {e}")

