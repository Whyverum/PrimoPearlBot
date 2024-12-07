# BotCode/routers/commands/user_cmd/__init__.py
# Инициализация пакета user_cmd, для работы с командами для пользователей

from aiogram import Router
from .start_cmd import router as start_router
from .help_cmd import router as help_router
from .more_cmd import router as more_router
from .exit_cmd import router as exit_router


# Объявление роутера и настройка экспорта
__all__ = ("router",)
router = Router(name="user_cmd_router")


# Список подключаемых роутеров сверху-вниз
router.include_routers(
    start_router,
    help_router,
    more_router,
    exit_router,
)
