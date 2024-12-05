# BotCode/routers/administration/__init__.py
# Инициализация пакета administration, для работы с функциями администратора
# Некоторые команды админов занесены в пакет commands в раздел admin_cmd

# Настройка экспорта модулей
__all__ = ("router",)

from aiogram import Router
from .admin_cmd import router as admin_cmd_router
from .easteggs_handlers import router as easteggs_router


# Создание роутера "admin_head_router"
router = Router(name="admin_head_router")


# Список подключаемых роутеров сверху-вниз
router.include_routers(
    admin_cmd_router,
    easteggs_router,
)
