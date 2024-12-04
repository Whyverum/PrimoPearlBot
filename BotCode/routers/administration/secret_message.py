# BotCode/routers/administration/secret_message.py

from aiogram import Router, types, F
from settings import *

# Создание роутера "secret_message_router"
router = Router(name="secret_message_router")
type_messages = "Admin"


# Хэндлер на текстовое сообщение "secret"
@router.message(F.from_user.id.in_(ListId.important_ids), F.text.lower() == "secret")
async def secret_admin_message(message: types.Message):
    text = f"Сообщение secret получено!"
    await message.reply(f"Привет, админ!")
    await logginger(message)
    logger.bind(custom_variable=type_messages, user_var=str(message.from_user.username)).info(text)
    return text
