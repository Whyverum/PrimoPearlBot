# BotCode/routers/commands/admin_cmd/__init__.py
# Инициализация пакета admin_cmd, для работы с админскими командами

from aiogram import Router
from .send_to_user import router as send_cmd_router
from .ban_cmd import router as ban_cmd_router
from .secret_cmd import router as secret_router
from .start_time_cmd import router as start_time_router


# Объявление роутера и настройка экспорта
__all__ = ("router",)
router = Router(name="admin_cmd_router")


# Список подключаемых роутеров сверху-вниз
router.include_routers(
    ban_cmd_router,
    secret_router,
    send_cmd_router,
)


# Идет самым последним, если другие роутеры не сработали
router.include_router(start_time_router)
