# BotCode/routers/downloads/__init__.py
# Инициализация пакета downloads, для работы с закачкой данных

from aiogram import Router
from .download_handlers import router as download_media_router

from .download_avatar_all import *
from .download_chat_avatar import *
from .download_user_avatar import *

# Объявление роутера и настройка экспорта модулей
__all__ = ("router", "download_avatar_all", "download_chat_avatar", "download_user_photos", "download_avatar")
router = Router(name="downloads_head_router")


# Список подключаемых роутеров сверху-вниз
router.include_routers(
    download_media_router,
)
