# BotCode/routers/common/messages.py   (Разберись с логгированием!!!!!)
# Нижний обработчик всех текстовых сообщений
# А также нескольких определенных сообщений (Перенести в иной файл!!!)

from BotLibrary import *
from aiogram import Router, types

from ..downloads.download_avatar_all import download_avatar

# Настройка экспорта модулей и роутера
__all__ = ("router",)
router = Router(name="common_message_router")

# Хэндлер на все сообщения и записывает данные
@router.message()
async def handle_all_messages(message: types.Message):
    log_type = "Messages"
    name = find_chat_id(message)
    message_type = types_message(message)

    await logginger(message)
    await download_avatar(message)

    await common_msg_logginger(message, name, message_type, log_type)
    return f"Получено новое сообщение!"
