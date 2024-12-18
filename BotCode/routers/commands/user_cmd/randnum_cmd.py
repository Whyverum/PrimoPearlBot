# BotCode/routers/commands/user_cmd/randnum_cmd.py
# Работа с командой /randnum, для рандомного числа с редактированием сообщения

from aiogram import Router, types, F
from aiogram.filters import Command
from BotLibrary import *
from keyboards.inline_kb.randnum_kb import get_randnum_kb

# Создание роутера и экспорта модулей
__all__ = ("router", "cmd_randnum", "log_type",)
router = Router(name="randnum_router")
log_type = "Randnum"

# Список ключевых слов для команды
keywords = ["кфтвтгь", "randnum",]


# Хэндлер на команду /randnum
@router.message(Command(*keywords, prefix=BotEdit.prefixs, ignore_case=True))
@router.message(F.text.lower().in_(keywords))
async def cmd_randnum(message: types.Message):
        text = "Работа с рандомом оценок!"
        await message.reply(
            text="Вы хотите узнать вашу оценку на сегодня?!",
            reply_markup=get_randnum_kb("Хочу: ТЫК"),
        )

        # Активация логгера
        await cmd_logginger(message, log_type, text)
        return text
