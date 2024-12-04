# more_cmd.py

from aiogram import Router, types
from aiogram.filters import Command
from settings import *
from BotCode.keyboards.more_kb import get_more_kb

# Создание роутера "more_router"
router = Router(name="more_router")
type_messages = "More"


# Хэндлер на команду /more
@router.message(Command("more", "ьщку", prefix=BotEdit.prefixs, ignore_case=True))
async def cmd_start(message: types.Message):
    text = "Команда /more с выпадающим списком активирована"
    await message.reply(text=f"Выпадающее меню для чего-нибудь:", reply_markup=get_more_kb())
    logger.bind(custom_variable=type_messages, user_var=str(message.from_user.username)).info(text)
    await logginger(message)
    return text
