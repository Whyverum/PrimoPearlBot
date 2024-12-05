# BotCode/main.py
# Основной код проекта, который и соединяет в себе все его возможности

import asyncio

from aiogram import Dispatcher
from datetime import datetime

from BotSettings import *
from BotCode.routers import router as main_router
from BotCode.routers import set_commands


# Запуск основного кода
async def main():
    # Подключение ANSI в стандартное Windows_cmd
    just_fix_windows_console()

    # Подключение маршрутизатора и получение важных переменных
    dp = Dispatcher()
    dp.include_router(main_router)
    dp["started_at"] = datetime.now().strftime("\n%Y-%m-%d %H:%M:%S")
    dp["is_active"] = True  # Флаг активности бота

    await set_all()     # Установка настроек бота
    await set_commands()    # Установка команд бота
    await bot_get_info()    # Получение информации о боте

    # Создание логгера и оповещение о запуске
    setup_logger()
    logger.bind(custom_variable="AEP", user_var="Console").info(f"Начало запуска бота @{BotInfo.username}...")

    # Включение опроса бота
    bot_info_out()
    await dp.start_polling(bot)


# Вечная загрузка бота
if __name__ == "__main__":  # Исправлено: правильное именование
    asyncio.run(main())
