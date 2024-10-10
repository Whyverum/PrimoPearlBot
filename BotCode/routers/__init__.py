# __init__.py

__all__ = ("router",)

from aiogram import Router
from BotCode.routers.administration.__init_admin__ import router as admins_router
from BotCode.routers.users.__init_user__ import router as users_router

router = Router(name=__name__)

router.include_routers(
    admins_router,
    users_router,
)
