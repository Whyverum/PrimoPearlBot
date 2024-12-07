# BotCode/routers/__init__.py
# Инициализация пакета routers, для работы с асинхронными обработчиками
# Пакет старых файлов отключен!!

# Импортируем библиотеки для экспорта
from aiogram import Router
from BotCode.routers.commands.bot_command import set_commands
from .administration import router as admin_head_router
from .commands import router as commands_head_router
from .downloads import router as downloads_head_router
from .common import router as users_head_router
# from .old_files import router as old_files_router


# Объявление главного роутера и настройка экспорта
__all__ = ("router", "set_commands",)
router = Router(name="main_router")


# Список подключаемых роутеров сверху-вниз
router.include_routers(
    admin_head_router,
    commands_head_router,
    downloads_head_router,
)


# Роутер, что запустится самым последним
router.include_router(users_head_router)
# router.include_router(old_files_router)
