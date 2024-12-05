# BotCode/routers/commands/user_cmd/start_cmd.py
# Работа с командой /start, для запуска бота

from aiogram import Router, types
from aiogram.filters import Command
from BotSettings import *
from BotCode.keyboards.start_kb import get_start_kb

# Создание роутера и настройка экспорта
__all__ = ("router", "cmd_start", "command_text",)
router = Router(name="start_router")
command_text = "Start"


# Обработчик команды /start
@router.message(Command("start", "старт", "запуск", "пуск", "on", "вкл", "с", "s", "ы",
                        "ыефке", "cnfhn", "pfgecr", "gecr", "щт", "drk", "restart", "куыефке",
                        prefix=BotEdit.prefixs, ignore_case=True))
async def cmd_start(message: types.Message):
    try:
        # Вывод сообщения пользователю
        text = f"использовал(а) команду /{command_text.lower()}"
        await message.reply(text=f"Стартовый бот!", reply_markup=get_start_kb())

        # Активация логгера
        await cmd_logginger(message, command_text, text)

        return text

    # Проверка на ошибку и ее логирование
    except Exception as e:
        text_error = await error_cmd_logginger(message, command_text, e)
        return text_error
