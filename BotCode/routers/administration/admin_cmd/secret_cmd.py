# BotCode/routers/administration/secret_cmd.py
# Проверка текста и команды "secret" для администраторов

from aiogram import Router, types, F
from aiogram.filters import Command
from BotLibrary import *

# Создание роутера и настройка экспорта модулей
__all__ = ("router",)

from routers.msg_default import msg_default

router = Router(name="secret_message_router")
log_type = "Admin"

# Список ключевых слов для команды
keywords = ["secret", "секрет", "ыускуе", "ctrhtn",
            "admin", "flvby", "админ", "фвьшт",]


# Обработчик команды /secret или сообщений с текстом из списка keywords
@router.message(F.from_user.id.func(lambda user_id: str(user_id) in DataID.important.keys()),
                Command(*keywords, prefix=BotVariables.prefixs, ignore_case=True))
@router.message(F.from_user.id.func(lambda user_id: str(user_id) in DataID.important.keys()),
                F.text.lower().in_(keywords))
async def secret_admin_message(message: types.Message):
    text = f"Привет, <b>важная персона</b>!"
    await message.reply(text)

    await cmd_logginger(message, log_type, text)
    await msg_default(message)
