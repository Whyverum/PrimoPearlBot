# BotCode/routers/commands/user_cmd/randnum_cmd.py
# Работа с командой /randnum, для рандомного числа с редактированием сообщения

from aiogram import Router, types, F
from aiogram.filters import Command
from BotLibrary import *
from BotCode.keyboards.inline_kb.randnum_kb import get_randnum_kb
from BotCode.routers.msg_default import msg_default

# Создание роутера, переменных и экспорта модулей
__all__ = ("router", "cmd_randnum", "log_type",)
router = Router(name="randnum_router")
log_type = "Randnum"
description = "Описание"

# Список ключевых слов для команды
keywords = ["кфтвтгь", "randnum",]

# Хэндлер на команду /randnum
@router.message(Command(*keywords, prefix=BotVariables.prefixs, ignore_case=True))
@router.message(F.text.lower().in_(keywords))
async def cmd_randnum(message: types.Message):
        text = "Работа с рандомом оценок!"
        await message.reply(
            text="Вы хотите узнать вашу оценку на сегодня?!",
            reply_markup=get_randnum_kb(),
        )

        # Активация логгера
        await cmd_logginger(message, log_type, text)
        await msg_default(message)
