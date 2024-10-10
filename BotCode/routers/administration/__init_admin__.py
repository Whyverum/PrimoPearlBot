# __init_admin__.py

__all__ = ("router",)

from aiogram import Router
from BotCode.routers.administration.admin_handlers import router as admin_router
from BotCode.routers.administration.analitics_handlers import router as analitic_router
from BotCode.routers.administration.send_message_handlers import router as send_router
from BotCode.routers.administration.ban_list import router as ban_list_router

router = Router(name=__name__)

router.include_routers(
    ban_list_router,
    analitic_router,
    send_router,
    admin_router,
)
