# BotCode/main.py
# Основной код проекта, который и соединяет в себе все его возможности

import asyncio
from BotLibrary import *
from BotCode.routers import router as main_router
from BotCode.routers import set_commands


# Запуск основного кода
async def main():
    # Создание логгера
    await setup_logger()

    # Подключение ANSI в стандартное Windows_cmd
    just_fix_windows_console()

    # Создание пустых директорий
    setup_directories()

    # Подключение главного маршрутизатора
    dp.include_router(main_router)

    await set_all()     # Установка настроек бота
    await set_commands()    # Установка команд бота
    await bot_get_info()    # Получение информации о боте

    # Оповещение о запуске с информацией бота
    logger.bind(log_type="AEP", user="Console").info(f"Начало запуска бота @{BotInfo.username}...")
    bot_info_out()

    # Включение опроса бота
    await bot.delete_webhook()
    await dp.start_polling(bot)


# Вечная загрузка бота
if __name__ == "__main__":  # Исправлено: правильное именование
    asyncio.run(main())
