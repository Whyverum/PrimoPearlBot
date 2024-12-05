# BotCode/routers/commands/admin_cmd/start_time_cmd.py
# Работа с командой /start_time, для вывода времени запуска бота

from aiogram import Router, types
from aiogram.filters import Command
from BotSettings import *

# Создание роутера и настройка экспорта
__all__ = ("router",)
router = Router(name="start_time_router")
command_text = "Start_Time"


# Хэндлер на команду /start_time
@router.message(Command("start_time", "stime", "старт_время", "время_старта", "с_время", "ыефке_ешьу", "ыешьу",
                    "cnfhn_dhtvcz", "dhtvz_cnfhnf", "c_dhtvz", prefix=BotEdit.prefixs, ignore_case=True))
async def start_time(message: types.Message, started_at: str):
    try:
        # Вывод сообщения пользователю
        text = f"использовал(а) команду /{command_text.lower()}"
        await message.answer(f"Бот @{BotInfo.username} запущен: <b>{started_at}</b>")

        # Активация логгера
        await cmd_logginger(message, command_text, text)

        return text

    # Проверка на ошибку и ее логирование
    except Exception as e:
        text_error = await error_cmd_logginger(message, command_text, e)
        return text_error

