# BotCode/routers/__init__.py

# Указываем, какие модули будут доступны через `import routers`
__all__ = ("router",)

# Импортируем библиотеки для экспорта
from aiogram import Router
from .administration import router as admin_head_router
from .commands import router as commands_head_router
from .downloads import router as downloads_head_router
from .users import router as users_head_router

# Объявление главного роутера
router = Router(name="main_router")


# Список подключаемых роутеров сверху-вниз
router.include_routers(
    admin_head_router,
    commands_head_router,
    downloads_head_router,
)

# Роутер, что запустится самым последним
router.include_router(users_head_router)
