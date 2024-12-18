# BotCode/routers/common/__init__.py
# Инициализация пакета common, для работы со всеми сообщениями

from aiogram import Router
from .messages import router as common_message_router


# Объявление роутера и настройка экспорта модулей
__all__ = ("router",)
router = Router(name="users_head_router")


# Список подключаемых роутеров сверху-вниз
router.include_routers(
    common_message_router,
)

# Идет самым последним, если другие роутеры не сработали
# router.include_router(common_message_router)
