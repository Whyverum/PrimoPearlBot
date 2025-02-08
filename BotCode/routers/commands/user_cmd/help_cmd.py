# BotCode/routers/commands/user_cmd/help_cmd.py
# Работа с командой /help, для вывода помощи пользователю

from aiogram import Router, types, F
from aiogram.filters import Command
from BotLibrary import *
from BotCode.keyboards.reply_kb.help_kb import get_help_kb
from BotCode.routers.msg_default import msg_default

# Создание роутера, переменных и экспорта модулей
__all__ = ("router", "cmd_help", "log_type", "description")
router = Router(name="help_router")
log_type = "Help"
description = "Получить помощь"

# Список ключевых слов для команды
keywords = ["help", "info", "помощь", "инфо", "?", "информация", "рудз", "штащ", "byaj",
            "gjvjom", "byajhvfwbz",]


# Хэндлер на команду /info или /help
@router.message(Command(*keywords, prefix=BotVariables.prefixs, ignore_case=True))
@router.message(F.text.lower().in_(keywords))
async def cmd_help(message: types.Message):
    try:
        # Вывод сообщения пользователю
        text = f"использовал(а) команду /{log_type.lower()}"
        await message.reply(
            text=f"Ну это типо привет. Ладно, это помощь.", reply_markup=get_help_kb())

        # Активация логгера
        await cmd_logginger(message, log_type, text)
        await msg_default(message)

    # Проверка на ошибку и ее логирование
    except Exception as e:
        text_error = await error_cmd_logginger(message, log_type, e)
        return text_error
