# BotCode/routers/__init__.py
# Инициализация пакета routers, для работы с асинхронными обработчиками

from aiogram import Router
from .callback_handlers import router as callback_handlers_router
from .commands.bot_command import set_commands
from .administration import router as admin_head_router
from .commands import router as commands_head_router
from .downloads import router as downloads_head_router
from .common import router as users_head_router


# Объявление главного роутера и настройка экспорта модулей
__all__ = ("router", "set_commands",)
router = Router(name="main_router")


# Список подключаемых роутеров сверху-вниз
router.include_routers(
callback_handlers_router,
    admin_head_router,
    commands_head_router,
    downloads_head_router,
)

# Роутер, что запустится самым последним
router.include_router(users_head_router)
