# BotCode/routers/commands/user_cmd/help_cmd.py
# Работа с командой /help, для вывода помощи пользователю

from aiogram import Router, types
from aiogram.filters import Command
from BotSettings import *
from BotCode.keyboards.help_kb import get_help_kb

# Создание роутера и экспорта
__all__ = ("router", "cmd_help", "command_text",)
router = Router(name="help_router")
command_text = "Help"


# Хэндлер на команду /info или /help
@router.message(Command("help", "info", "помощь", "инфо", "?", "информация", "рудз", "штащ", "byaj",
                    "gjvjom", "byajhvfwbz", prefix=BotEdit.prefixs, ignore_case=True))
async def cmd_help(message: types.Message):
    try:
        # Вывод сообщения пользователю
        text = f"использовал(а) команду /{command_text.lower()}"
        await message.reply(
            text=f"Ну это типо привет. Ладно, это помощь.", reply_markup=get_help_kb())

        # Активация логгера
        await cmd_logginger(message, command_text, text)

        return text

    # Проверка на ошибку и ее логирование
    except Exception as e:
        text_error = await error_cmd_logginger(message, command_text, e)
        return text_error
