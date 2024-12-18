# BotCode/routers/commands/user_cmd/help_cmd.py
# Работа с командой /help, для вывода помощи пользователю

from aiogram import Router, types, F
from aiogram.filters import Command
from BotLibrary import *
from BotCode.keyboards.help_kb import get_help_kb

# Создание роутера и экспорта модулей
__all__ = ("router", "cmd_help", "log_type",)
router = Router(name="help_router")
log_type = "Help"

# Список ключевых слов для команды
keywords = ["help", "info", "помощь", "инфо", "?", "информация", "рудз", "штащ", "byaj",
            "gjvjom", "byajhvfwbz",]


# Хэндлер на команду /info или /help
@router.message(Command(*keywords, prefix=BotEdit.prefixs, ignore_case=True))
@router.message(F.text.lower().in_(keywords))
async def cmd_help(message: types.Message):
    try:
        # Вывод сообщения пользователю
        text = f"использовал(а) команду /{log_type.lower()}"
        await message.reply(
            text=f"Ну это типо привет. Ладно, это помощь.", reply_markup=get_help_kb())

        # Активация логгера
        await cmd_logginger(message, log_type, text)
        return text

    # Проверка на ошибку и ее логирование
    except Exception as e:
        text_error = await error_cmd_logginger(message, log_type, e)
        return text_error