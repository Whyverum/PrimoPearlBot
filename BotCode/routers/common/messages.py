# BotCode/routers/common/messages.py   (Разберись с логгированием!!!!!)
# Нижний обработчик всех текстовых сообщений
# А также нескольких определенных сообщений (Перенести в иной файл!!!)

from BotLibrary import *
from aiogram import Router, types
from routers.msg_default import *

# Настройка экспорта модулей и роутера
__all__ = ("router",)
router = Router(name="common_message_router")
log_type = "Messages"


# Хэндлер на все сообщения и записывает данные
@router.message()
async def handle_all_messages(message: types.Message):
    user_name = find_imp_id(message.from_user.id)
    message_type = types_message(message)

    await common_msg_logginger(message, user_name, message_type, log_type)
    await msg_default(message)
