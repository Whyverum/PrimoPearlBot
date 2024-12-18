# BotCode/keyboards/__init__.py
# Инициализация пакета keyboards, для работы с клавиатурами

from aiogram import Router
from .actor_kb import *
from .randnum_kb import *

# Объявление роутера и настройка экспорта модулей
__all__ = ("router", "actor_kb", "ButtonInl")
router = Router(name="inline_kb_router")


# Список подключаемых роутеров сверху-вниз
# router.include_routers()
