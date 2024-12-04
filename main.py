# BotCode/main.py

import asyncio
from aiogram import Dispatcher
from datetime import datetime

from settings import *
from BotCode.routers import router as main_router
from BotCode.routers.commands.bot_command import set_commands


# Запуск основного кода
async def main():
    # Подключение ANSI в стандартное Windows_cmd
    just_fix_windows_console()

    # Объявление диспатчера
    dp = Dispatcher()

    # Установка автономных настроек
    await set_all()

    # Установка списка команд бота
    await set_commands()

    # Подключение маршрутизатора
    dp.include_router(main_router)

    # Переменная времени включения бота
    dp["started_at"] = datetime.now().strftime("%Y-%m-%d %H:%M")

    # Создание логгера и оповещение о запуске
    setup_logger()
    logger.bind(custom_variable="AEP", user_var="Console").info(f"Начало запуска бота @{BotInfo.username}...")
    logger.bind(custom_variable="AEP", user_var="Console").error(f"Начало запуска бота @{BotInfo.username} не зашло")

    # Включение опроса бота
    await bot_info_out()
    await dp.start_polling(bot)


# Вечная загрузка бота
if __name__ == "__main__":  # Исправлено: правильное именование
    asyncio.run(main())
