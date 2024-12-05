# BotCode/routers/downloads/download_avatar_all.py
# Объединение закачки аватаров всех типов

from BotCode.routers.downloads.download_chat_avatar import download_chat_avatar
from BotCode.routers.downloads.download_user_avatar import download_user_photos


# Функция объединения закачки аватарок
async def download_avatar(message):
    await download_chat_avatar(message.chat)
    await download_user_photos(message)
    return f"Успешная закачка аватаров!"
