# BotCode/routers/commands/user_cmd/more_cmd.py
# Работа с командой /more, для вывода различных клавиатур

from aiogram import Router, types, F
from aiogram.filters import Command
from BotLibrary import *
from BotCode.keyboards.reply_kb.more_kb import get_more_kb
from BotCode.routers.msg_default import msg_default

# Создание роутера, переменных и экспорта модулей
__all__ = ("router", "cmd_start", "log_type",)
router = Router(name="more_router")
log_type = "More"
description = "Описание"

# Список ключевых слов для команды
keywords = ["more", "ьщку",]


# Обработчик команды /more
@router.message(Command(*keywords, prefix=BotVariables.prefixs, ignore_case=True))
@router.message(F.text.lower().in_(keywords))
async def cmd_start(message: types.Message):
    try:
        # Вывод сообщения пользователю
        text = f"использовал(а) команду /{log_type.lower()}"
        await message.reply(text=f"Выпадающее меню для чего-нибудь:", reply_markup=get_more_kb())

        # Активация логгера
        await cmd_logginger(message, log_type, text)
        await msg_default(message)

    # Проверка на ошибку и ее логирование
    except Exception as e:
        text_error = await error_cmd_logginger(message, log_type, e)
        return text_error
