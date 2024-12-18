# BotCode/routers/commands/__init__.py
# Инициализация пакета commands, для работы с командами бота

from aiogram import Router
from .bot_command import router as bot_command_router
from .user_cmd import router as user_cmd_router


# Объявление роутера и настройка экспорта модулей
__all__ = ("router",)
router = Router(name="commands_head_router")


# Список подключаемых роутеров сверху-вниз
router.include_routers(
    bot_command_router,
    user_cmd_router,
)
