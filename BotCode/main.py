# main.py

import asyncio
import sys

from loguru import logger
from aiogram import Dispatcher

from BotCode import config
from BotCode.routers import router as main_router
from BotCode.routers.administration.analitics_handlers import write_bot_start_info


logs = ""
logger.remove()
logger.add("BotInfo/bot.log", rotation="500 MB", backtrace=True, diagnose=True, format=logs)
logs = config.logs
logger.info("\n"), logger.info("\n"), logger.info("\n")
logger.add(sys.stdout, colorize=True, format=logs)


async def main():
    dp = Dispatcher()
    dp.include_router(main_router)
    bot = config.bots
    await config.get_info(bot)
    logger.bind(custom_variable="AEP", user_var="Console").info(f"Начало запуска бота @{config.bot_username}...")
    await write_bot_start_info()
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
