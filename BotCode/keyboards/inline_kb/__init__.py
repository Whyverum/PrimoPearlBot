# BotCode/keyboards/inline_kb/__init__.py
# Инициализация пакета inline_keyboards, для работы с инлайн клавиатурами

from aiogram import Router
from .actor_kb import *
from .randnum_kb import *

# Объявление роутера и настройка экспорта модулей
__all__ = ("router", "actor_kb", "ButtonInl")
router = Router(name="inline_kb_router")
