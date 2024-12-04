# routers/commands/admin_cmd/start_time.py

from aiogram import Router, types
from aiogram.filters import Command
from settings import BotEdit

router = Router(name="start_time_router")
type_messages = "Start_Time"


# Хэндлер на команду /start_timex
@router.message(Command("start_time", "stime", "старт_время", "время_старта", "с_время", "ыефке_ешьу", "ыешьу",
                    "cnfhn_dhtvcz", "dhtvz_cnfhnf", "c_dhtvz", prefix=BotEdit.prefixs, ignore_case=True))
async def start_time(message: types.Message, started_at: str):
    text = f"Бот запущен {started_at}"
    await message.answer(text)
    return text
