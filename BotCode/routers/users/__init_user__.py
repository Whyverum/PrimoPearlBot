# __init_user__.py

__all__ = ("router",)

from aiogram import Router
from BotCode.routers.users.start_cmd import router as start_router
from BotCode.routers.users.common import router as common_router
from BotCode.routers.users.download_handlers import router as download_router
from BotCode.routers.users.easteggs_handlers import router as easteggs_router


router = Router(name=__name__)

router.include_routers(
    start_router,
    download_router,
    easteggs_router,
    common_router
)
