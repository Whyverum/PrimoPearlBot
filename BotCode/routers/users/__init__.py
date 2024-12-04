# __init__.py

# Импортирование модуля роутера при *
__all__ = ("router",)

from aiogram import Router
from .messages import router as common_message_router

# Объявление роутера users_router
router = Router(name="users_head_router")


# Идет самым последним, если другие роутеры не сработали
router.include_router(common_message_router)
