# BotCode/routers/commands/admin_cmd/__init__.py
# Инициализация пакета admin_cmd, для работы с админскими командами

from aiogram import Router
from .secret_cmd import router as secret_router


# Объявление роутера и настройка экспорта модулей
__all__ = ("router",)
router = Router(name="admin_cmd_router")


# Список подключаемых роутеров сверху-вниз
router.include_routers(
    secret_router,
)
