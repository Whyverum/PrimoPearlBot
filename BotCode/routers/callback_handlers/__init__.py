from aiogram import Router

from .actor_kb_cb import router as actor_kb_cb_router
from .randnum_kb_cb import router as randnum_kb_cb_router

__all__ = ("router", )
router = Router(name="callback_handlers")

# Список подключаемых роутеров сверху-вниз
router.include_routers(
    actor_kb_cb_router,
    randnum_kb_cb_router,
)
