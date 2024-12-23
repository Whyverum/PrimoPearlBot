# BotCode/routers/downloads/download_chat_avatar.py
# Функция скачивания аватара чата

import os
import aiohttp
from BotLibrary import *

# Создание роутера и настройка экспорта модулей
__all__ = ("download_chat_avatar",)
log_type = "AvatarChat"


# Функция закачки аватарок чатов
async def download_chat_avatar(message):
    try:
        chat = message.chat
        # Проверка типа чата (группа или супергруппа)
        if chat.type in ["group", "supergroup"]:
            chat_info = await bot.get_chat(chat.id)

            # Проверка на наличие фотографий чата
            if not chat_info.photo:
                text_error = f"Чат с ID {chat.id} не имеет аватара."
                logger.bind(log_type=log_type, user=chat.id).error(text_error)
                return text_error

            file_id = (
                    getattr(chat_info.photo, 'big_file_id', None) or
                    getattr(chat_info.photo, 'medium_file_id', None) or
                    getattr(chat_info.photo, 'small_file_id', None)
            )

            if not file_id:
                text_error = f"Не удалось получить file_id аватара чата с ID {chat.id}."
                logger.bind(log_type=log_type, user=chat.id).error(text_error)
                return text_error

            file_info = await bot.get_file(file_id)
            file_url = f"https://api.telegram.org/file/bot{bot.token}/{file_info.file_path}"

            chat_id = find_imp_id(chat.id)
            save_dir = f"{ProjectPath.chat_avatar}/{chat_id}"
            os.makedirs(save_dir, exist_ok=True)

            file_extension = os.path.splitext(file_info.file_path)[-1]
            file_name = f"avatar{file_extension}"
            save_path = os.path.join(save_dir, file_name)

            # Асинхронное скачивание
            async with aiohttp.ClientSession() as session:
                async with session.get(file_url) as response:
                    if response.status == 200:
                        with open(save_path, "wb") as file:
                            while True:
                                chunk = await response.content.read(8192)
                                if not chunk:
                                    break
                                file.write(chunk)
                        return f"Фото аватара чата с ID {chat_id} успешно скачано."
                    else:
                        text_error = f"Не удалось скачать фото аватара чата с ID {chat_id}. Статус: {response.status}"
                        logger.bind(log_type=log_type, user=chat.id).error(text_error)
                        return text_error
        else:
            return

    except Exception as e:
        chat = message.chat
        text_error = f"Ошибка при скачивании фото аватара чата с ID {chat.id}: {e}"
        logger.bind(log_type=log_type, user=chat.id).error(text_error)
        return text_error
