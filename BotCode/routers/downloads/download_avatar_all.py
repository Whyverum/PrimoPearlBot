# BotCode/routers/downloads/download_avatar_all.py
# Объединение закачки аватаров всех типов
from BotLibrary import write_user_info_to_file
from .download_chat_avatar import download_chat_avatar
from .download_user_avatar import download_user_photos

# Настройка экспорта модулей
__all__ = ("download_avatar", "download_chat_avatar", "download_user_photos")


# Функция объединения закачки аватарок
async def download_avatar(message):
    await download_chat_avatar(message)
    await download_user_photos(message)
    write_user_info_to_file(message.from_user)
