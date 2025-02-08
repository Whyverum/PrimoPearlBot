# BotCode/routers/survey/__init__.py
# Инициализация пакета survey, для работы с закачкой данных

from aiogram import Router
from .handlers import router as handlers_router

# Объявление роутера и настройка экспорта модулей
__all__ = ("router", )
router = Router(name="survey_head_router")


# Список подключаемых роутеров сверху-вниз
router.include_routers(
    handlers_router,
)
