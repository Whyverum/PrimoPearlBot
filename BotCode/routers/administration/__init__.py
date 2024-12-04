# __init__.py

__all__ = ("router",)

from aiogram import Router
from .secret_message import router as secret_message_router
from .easteggs_handlers import router as easteggs_router

router = Router(name="admin_head_router")

# Список подключаемых роутеров сверху-вниз
router.include_routers(
    secret_message_router,
    easteggs_router,
)
