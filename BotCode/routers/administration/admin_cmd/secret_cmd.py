# BotCode/routers/administration/secret_cmd.py
# Проверка текст и команду "secret" для администраторов

from aiogram import Router, types, F
from aiogram.filters import Command
from BotSettings import *

# Создание роутера и настройка экспорта
__all__ = ("router",)
router = Router(name="secret_message_router")
type_messages = "Admin"


# Обработчик команды /start
@router.message(Command("secret", "секрет", "ыускуе", "ctrhtn", "admin", "flvby", "админ", "фвьшт",
                        prefix=BotEdit.prefixs, ignore_case=True))
@router.message(F.from_user.id.in_(ListId.important_ids), F.text.lower() == "secret")
async def secret_admin_message(message: types.Message):
    text = f"Привет, админ!"
    await message.reply(text)
    await logginger(message)
    logger.bind(custom_variable=type_messages, user_var=str(message.from_user.username)).info(text)
    return text
