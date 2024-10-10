# start_cmd.py

from aiogram import Router, types
from aiogram.filters import Command

from loguru import logger

from BotCode.routers.administration.analitics_handlers import loginger
from BotCode import config

router = Router(name=__name__)


# Хэндлер на команду /start или /старт
@router.message(Command("start", "старт", "запуск", "пуск", "on", "вкл",
                        prefix=config.prefix, ignore_case=True))
async def cmd_start(message: types.Message):
    logger.bind(custom_variable="Start", user_var=str(message.from_user.username)).info("Команда /start активирована")
    await message.reply(text=f"Стартовый бот!")
    await loginger(message)


# Хэндлер на команду /info или /help
@router.message(Command("help", "info", "помощь", "инфо", "?", "информация",
                        prefix=config.prefix, ignore_case=True))
async def cmd_help(message: types.Message):
    logger.bind(custom_variable="Help", user_var=str(message.from_user.username)).info("Команда /help активирована")
    await message.answer(text=f"Вижу команду!")
    await loginger(message)
