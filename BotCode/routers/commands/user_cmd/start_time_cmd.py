# BotCode/routers/commands/admin_cmd/start_time_cmd.py
# Работа с командой /start_time, для вывода времени запуска бота

from aiogram import Router, types, F
from aiogram.filters import Command
from BotLibrary import *
from BotCode.routers.msg_default import msg_default

# Создание роутера, переменных и настройка экспорта модулей
__all__ = ("router", "start_time", "log_type", "description")
router = Router(name="start_time_router")
log_type = "Start_Time"
description = "Время запуска"

# Список ключевых слов для команды
start_time_keywords = ["start_time", "stime", "старт_время", "время_старта", "с_время",
                       "ыефке_ешьу", "ыешьу", "cnfhn_dhtvcz", "dhtvz_cnfhnf", "c_dhtvz", 
                       "бот_время", "время_запуска", "бот_врем"]


# Хэндлер на команду /start_time
@router.message(Command(*start_time_keywords, prefix=BotVariables.prefixs, ignore_case=True))
@router.message(F.text.lower().in_(start_time_keywords))
async def start_time(message: types.Message, started_at: str, started_at_msk: str):
    try:
        # Вывод сообщения пользователю
        text = f"использовал(а) команду /{log_type.lower()}"
        await message.answer(f"Бот @{BotInfo.username} запущен: "
                             f"\nХост: <b>{started_at}</b>"
                             f"\nМСК: <b>{started_at_msk}</b>")

        # Активация логгера
        await cmd_logginger(message, log_type, text)
        await msg_default(message)

    # Проверка на ошибку и ее логирование
    except Exception as e:
        error_text = await error_cmd_logginger(message, log_type, e)
        return error_text

