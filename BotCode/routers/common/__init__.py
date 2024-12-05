# BotCode/routers/common/__init__.py
# Инициализация пакета common, для работы со всеми сообщениями

# Настройка экспорта модулей
__all__ = ("router",)

from aiogram import Router
from .messages import router as common_message_router


# Объявление роутера "users_head_router"
router = Router(name="users_head_router")


# Идет самым последним, если другие роутеры не сработали
router.include_router(common_message_router)
