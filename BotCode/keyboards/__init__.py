# BotCode/keyboards/__init__.py
# Инициализация пакета keyboards, для работы с клавиатурами

# Импортируем библиотеки для экспорта
from aiogram import Router
from .start_kb import router as start_kb_router
from .help_kb import router as help_kb_router
from .more_kb import router as more_kb_router


# Объявление роутера и настройка экспорта
__all__ = ("router",)
router = Router(name="kb_router")


# Список подключаемых роутеров сверху-вниз
router.include_routers(
    start_kb_router,
    help_kb_router,
    more_kb_router,
)
