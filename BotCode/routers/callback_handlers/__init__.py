# BotCode/routers/callback_handlers/__init__.py
# Инициализация пакета callback_handlers, для работы с запросами бота

from aiogram import Router
from .actor_kb_cb import router as actor_kb_cb_router
from .randnum_kb_cb import router as randnum_kb_cb_router

# Объявление роутера и настройка экспорта модулей
__all__ = ("router", )
router = Router(name="callback_handlers")


# Список подключаемых роутеров сверху-вниз
router.include_routers(
    actor_kb_cb_router,
    randnum_kb_cb_router,
)
