# BotCode/MySQL/__init__.py

# Указываем, какие модули будут доступны через `import keyboards`
__all__ = ("router", "db")

# Импортируем библиотеки для экспорта
from aiogram import Router
from .db import *

# Создание роутера sql_router
router = Router(name="sql_router")

# Список подключаемых роутеров сверху-вниз
router.include_routers()
