# BotCode/routers/commands/user_cmd/start_cmd.py
# Работа с командой /start, для запуска бота

from aiogram import Router, types, F
from aiogram.filters import Command
from BotLibrary import *
from BotCode.keyboards.start_kb import get_start_kb

# Создание роутера и настройка экспорта модулей
__all__ = ("router", "cmd_start", "log_type",)
router = Router(name="start_router")
log_type = "Start"

# Список ключевых слов для команды
keywords = ["start", "старт", "запуск", "пуск", "on", "вкл", "с", "s", "ы",
            "ыефке", "cnfhn", "pfgecr", "gecr", "щт", "drk", "restart", "куыефке",]


# Обработчик команды /start
@router.message(Command(*keywords, prefix=BotEdit.prefixs, ignore_case=True))
@router.message(F.text.lower().in_(keywords))
async def cmd_start(message: types.Message):
    try:
        # Вывод сообщения пользователю
        text = f"использовал(а) команду /{log_type.lower()}"
        await message.reply(text=f"Стартовый бот!", reply_markup=get_start_kb())

        # Активация логгера
        await cmd_logginger(message, log_type, text)
        return text

    # Проверка на ошибку и ее логирование
    except Exception as e:
        text_error = await error_cmd_logginger(message, log_type, e)
        return text_error
