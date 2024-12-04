# __init__.py

__all__ = ("router",)

from aiogram import Router

router = Router(name="old_files_router")


# Список подключаемых роутеров сверху-вниз
router.include_routers()
