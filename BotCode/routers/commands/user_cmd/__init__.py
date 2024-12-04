# __init__.py

# Импортирование модуля роутера при *
__all__ = ("router",)

from aiogram import Router
from .start_cmd import router as start_router
from .help_cmd import router as help_router
from .more_cmd import router as more_router
from .exit_cmd import router as exit_router

# Создание роутера "user_cmd_router"
router = Router(name="user_cmd_router")


# Список подключаемых роутеров сверху-вниз
router.include_routers(
    start_router,
    help_router,
    more_router,
    # exit_router,
)
