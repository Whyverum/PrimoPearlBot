# BotCode/keyboards/reply_kb/__init__.py
# Инициализация пакета reply_kb, для работы с клавиатурами

from aiogram import Router
from .help_kb import router as help_kb_router


# Объявление роутера и настройка экспорта модулей
__all__ = ("router",)
router = Router(name=__name__)


# Список подключаемых роутеров сверху-вниз
router.include_routers(help_kb_router)
