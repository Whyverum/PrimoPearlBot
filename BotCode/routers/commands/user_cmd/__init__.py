# BotCode/routers/commands/user_cmd/__init__.py
# Инициализация пакета user_cmd, для работы с командами для пользователей

from aiogram import Router
from .start_cmd import router as start_router
from .help_cmd import router as help_router
from .more_cmd import router as more_router
from .exit_cmd import router as exit_router
from .start_time_cmd import router as start_time_router
from .actor_cmd import router as actor_router
from .randnum_cmd import router as randnum_router


# Объявление роутера и настройка экспорта модулей
__all__ = ("router",)
router = Router(name="user_cmd_router")


# Список подключаемых роутеров сверху-вниз
router.include_routers(
    start_router,
    help_router,
    more_router,
    exit_router,
    actor_router,
    randnum_router,
)


# Идет самым последним, если другие роутеры не сработали
router.include_router(start_time_router)
