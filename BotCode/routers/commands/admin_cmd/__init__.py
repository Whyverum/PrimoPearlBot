# __init__.py

__all__ = ("router",)

from aiogram import Router
from .send_to_user import router as send_cmd_router
from .ban_cmd import router as ban_cmd_router
from .start_time import router as start_time_router

# Создание роутера "admin_cmd_router"
router = Router(name="admin_cmd_router")


# Список подключаемых роутеров сверху-вниз
router.include_routers(
    ban_cmd_router,
    send_cmd_router,
)


# Идет самым последним, если другие роутеры не сработали
router.include_router(start_time_router)
