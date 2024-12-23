# MySQL/__init__.py
# Инициализация пакета MySQL, для работы с базой данных    (в разработке)

# Настройка экспорта модулей
__all__ = ("router", "db")

# Импортируем библиотеки для экспорта
from aiogram import Router


# Создание роутера "sql_router"
router = Router(name="sql_router")
