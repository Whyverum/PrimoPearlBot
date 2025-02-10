# BotCode/routers/commands/user_cmd/time_cmd.py
# Работа с командой /time, для вывода времени

from aiogram import Router, types
from aiogram.filters import Command
from BotLibrary import *
from BotCode.routers.msg_default import msg_default

# Создание роутера, переменных и настройка экспорта модулей
__all__ = ("router", "cmd_time", "log_type", "description")
router = Router(name="time_cmd_router")
log_type = "Time"
description = "Мировое время"

# Список ключевых слов для команды
keywords = ["time", "ешьу", "dhtvz", "время"]


# Обработчик команды /time
@router.message(Command(*keywords, prefix=BotVariables.prefixs, ignore_case=True))
async def cmd_time(message: types.Message):
    try:
        # Получаем текущее время для Москвы и Красноярска
        current_time_msk = get_choice_time(TimeVariable.choice_utc_msk)
        current_time_krsk = get_choice_time(TimeVariable.choice_utc_krsk)

        # Формируем текст для ответа
        text = (
            f"Текущее время в Москве: \n<b>{current_time_msk}</b>\n"
            f"Текущее время в Красноярске: \n<b>{current_time_krsk}</b>"
        )

        # Отправляем сообщение пользователю
        await message.reply(text)

        # Активация логгера
        await cmd_logginger(message, log_type, text)
        await msg_default(message)

    except Exception as e:
        # Логирование ошибки
        text_error = await error_cmd_logginger(message, log_type, e)
        return text_error