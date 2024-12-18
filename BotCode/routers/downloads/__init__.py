# BotCode/routers/downloads/__init__.py
# Инициализация пакета downloads, для работы с закачкой данных

from aiogram import Router
from .download_handlers import router as download_media_router
from .download_user_avatar import router as user_avatar_router

# Объявление роутера и настройка экспорта модулей
__all__ = ("router",)
router = Router(name="downloads_head_router")


# Список подключаемых роутеров сверху-вниз
router.include_routers(
    download_media_router,
    user_avatar_router,
)
