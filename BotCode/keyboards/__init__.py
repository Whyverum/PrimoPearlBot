# BotCode/keyboards/__init__.py
# Инициализация пакета keyboards, для работы с клавиатурами

from aiogram import Router
from .inline_kb import router as inline_kb_router
from .reply_kb import router as reply_kb_router
from .inline_kb import *
from .reply_kb import *

# Объявление роутера и настройка экспорта модулей
__all__ = ("router", "inline_kb", "reply_kb",)
router = Router(name="kb_router")


# Список подключаемых роутеров сверху-вниз
router.include_routers(
    inline_kb_router,
    reply_kb_router,
)
