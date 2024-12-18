import os
import requests
from aiogram import Router
from aiogram.types import Chat
from BotLibrary import *

# Создание роутера и настройка экспорта модулей
__all__ = ("router", "download_chat_avatar",)
router = Router(name="avatar_chat_router")
log_type = "AvatarChat"


# Функция закачки аватарок чатов
async def download_chat_avatar(message, chat: Chat):
    try:
        # Проверка типа чата (группа или супергруппа)
        if chat.type in ["group", "supergroup"]:
            # Получаем информацию о чате (включая фото)
            chat_info = await bot.get_chat(chat.id)

            chat_id = chat.id

            # Проверка наличия аватара
            if not chat_info.photo:
                text_error = f"Чат с ID {chat_id} не имеет аватара."
                logger.bind(log_type=log_type, user=chat_id).error(text_error)
                return text_error

            # Получаем file_id для фото (высокое качество приоритетно)
            file_id = (
                    getattr(chat_info.photo, 'big_file_id', None) or
                    getattr(chat_info.photo, 'medium_file_id', None) or
                    getattr(chat_info.photo, 'small_file_id', None)
            )

            if not file_id:
                text_error = f"Не удалось получить file_id аватара чата с ID {chat_id}."
                logger.bind(log_type=log_type, user=chat_id).error(text_error)
                return text_error

            # Получаем file_info для фото
            file_info = await bot.get_file(file_id)

            # Строим URL для скачивания файла
            file_url = f"https://api.telegram.org/file/bot{bot.token}/{file_info.file_path}"

            # Формируем путь для сохранения фото
            chat_id = find_chat_id(message)
            save_dir = f"{ImportantPath.chat_avatar}/{chat_id}"
            os.makedirs(save_dir, exist_ok=True)

            file_extension = os.path.splitext(file_info.file_path)[-1]
            file_name = f"avatar{file_extension}"
            save_path = os.path.join(save_dir, file_name)

            # Скачиваем аватар
            response = requests.get(file_url, stream=True)
            if response.status_code == 200:
                with open(save_path, "wb") as file:
                    for chunk in response.iter_content(chunk_size=8192):
                        file.write(chunk)
                return f"Фото аватара чата с ID {chat_id} успешно скачано."

            else:
                text_error = f"Не удалось скачать фото аватара чата с ID {chat_id}. Статус: {response.status_code}"
                logger.bind(log_type=log_type, user=chat_id).error(text_error)
                return text_error

    except Exception as e:
        text_error = f"Ошибка при скачивании фото аватара чата с ID {chat.id}: {e}"
        logger.bind(log_type=log_type, user=chat.id).exception(text_error)
        return text_error
