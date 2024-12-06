# BotCode/routers/downloads/download_chat_avatar.py
# Закачка аватарок чата (починить качество + сделать логирование!!!)

import requests
from aiogram import Router
from aiogram.types import Chat
from BotSettings import *

# Создание роутера и настройка экспорта
__all__ = ("router", "download_chat_avatar",)
router = Router(name="avatar_chat_router")
type_messages = "AvatarChat"


# Функция закачки аватарок чатов
async def download_chat_avatar(message, chat: Chat):
    try:
        # Проверка типа чата (группа или супергруппа)
        if chat.type in ["group", "supergroup"]:
            # Получаем информацию о чате (включая фото)
            chat_info = await bot.get_chat(chat.id)

            chat_id = chat.id  # Используем chat.id напрямую
            # Проверка наличия аватара
            if not chat_info.photo:
                text_error = f"Чат с ID {chat_id} не имеет аватара."
                return text_error

            # Получаем file_id для фото (используем самое большое доступное изображение)
            # Мы пытаемся получить изображение в лучшем разрешении (если оно существует)
            file_id = chat_info.photo.big_file_id if chat_info.photo.big_file_id else (
                chat_info.photo.medium_file_id if chat_info.photo.medium_file_id else chat_info.photo.small_file_id
            )

            # Получаем file_info для фото
            file_info = await bot.get_file(file_id)

            # Строим URL для скачивания файла
            file_url = f"https://api.telegram.org/file/bot{bot.token}/{file_info.file_path}"

            # Формируем имя и путь для сохранения фото
            save_dir = f"{ImportantPath.chat_avatar}/{chat_id}"
            os.makedirs(save_dir, exist_ok=True)
            file_name = file_info.file_path.split("/")[-1]  # Имя файла (например, "abc.jpg")
            save_path = os.path.join(save_dir, file_name)

            # Скачиваем аватар
            response = requests.get(file_url)
            if response.status_code == 200:
                with open(save_path, "wb") as file:
                    file.write(response.content)
                text = f"Фото аватара чата с ID {chat_id} успешно скачано и сохранено как {save_path}"
                return text

            else:
                text_error = f"Не удалось скачать фото аватара чата с ID {chat_id}. Статус: {response.status_code}"
                logger.bind(custom_variable=type_messages, user_var=f"{chat_id}").error(text_error)
                return text_error

    # Проверка на ошибку закачки аватара чата
    except Exception as e:
        text_error = f"Ошибка при скачивании фото аватара чата с ID {chat.id}: {e}"
        logger.bind(custom_variable=type_messages, user_var=f"{chat.id}").error(text_error)
        return text_error
