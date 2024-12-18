# BotCode/routers/administration/__init__.py
# Инициализация пакета administration, для работы с функциями администратора
# Некоторые команды админов занесены в пакет commands в раздел admin_cmd

from aiogram import Router
from .admin_cmd import router as admin_cmd_router
from .easteggs_handlers import router as easteggs_router


# Объявление роутера и настройка экспорта модулей
__all__ = ("router",)
router = Router(name="admin_head_router")


# Список подключаемых роутеров сверху-вниз
router.include_routers(
    admin_cmd_router,
    easteggs_router,
)
