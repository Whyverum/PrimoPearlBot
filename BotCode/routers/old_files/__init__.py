# BotCode/routers/old_files/__init__.py
# Инициализация старого пакета old_files, для хранения старых функций

# Настройка экспорта модулей
__all__ = ("router",)

from aiogram import Router
from .media_func import router as media_old_router
from .regular_handlers import router as regular_router


# Объявление роутера "old_files_router"
router = Router(name="old_files_router")


# Список подключаемых роутеров сверху-вниз
router.include_routers(
    regular_router,
    media_old_router,
)


# Список подключаемых роутеров сверху-вниз
router.include_routers()
