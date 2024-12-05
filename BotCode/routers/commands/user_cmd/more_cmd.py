# BotCode/routers/commands/user_cmd/more_cmd.py
# Работа с командой /more, для вывода различных клавиатур

from aiogram import Router, types
from aiogram.filters import Command
from BotSettings import *
from BotCode.keyboards.more_kb import get_more_kb

# Создание роутера и экспорта
__all__ = ("router", "cmd_start",)
router = Router(name="more_router")
command_text = "More"


# Обработчик команды /more
@router.message(Command("more", "ьщку", prefix=BotEdit.prefixs, ignore_case=True))
async def cmd_start(message: types.Message):
    try:
        # Вывод сообщения пользователю
        text = f"использовал(а) команду /{command_text.lower()}"
        await message.reply(text=f"Выпадающее меню для чего-нибудь:", reply_markup=get_more_kb())

        # Активация логгера
        await cmd_logginger(message, command_text, text)

        return text

    # Проверка на ошибку и ее логирование
    except Exception as e:
        text_error = await error_cmd_logginger(message, command_text, e)
        return text_error
