# __init__.py

# Импортирование модуля роутера при *
__all__ = ("router",)

from aiogram import Router
from .bot_command import router as bot_command_router
from .admin_cmd import router as admin_cmd_router
from .user_cmd import router as user_cmd_router

# Объявление роутера commands_router
router = Router(name="commands_head_router")


# Список подключаемых роутеров сверху-вниз
router.include_routers(
    bot_command_router,
    admin_cmd_router,
    user_cmd_router,
)
