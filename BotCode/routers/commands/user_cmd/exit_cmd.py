# BotCode/routers/commands/user_cmd/exit_cmd.py
# Работа с командой /exit, для покидания чата   (в разработке)

from aiogram import Router, types, F
from aiogram.filters import Command
from BotLibrary import *
from routers.msg_default import msg_default

# Создание роутера, переменных и экспорта модулей
__all__ = ("router", "exit_cmd", "log_type", "description")
router = Router(name="exit_router")
log_type = "Exit"
description = "Выйти из чата (в разработке)"

# Список ключевых слов для команды
keywords = ["выход", "ds[j;", "exit", "учше",]


# Обработчик команды /exit
@router.message(Command(*keywords, prefix=BotVariables.prefixs, ignore_case=True))
@router.message(F.text.lower().in_(keywords))
async def exit_cmd(message: types.Message):
    try:
        # Вывод сообщения пользователю и его блокировка
        text = f"Пользователь {message.from_user.id} успешно вышел из чата!"
        await message.reply(text)
        await bot.ban_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)

        # Активация логгера
        await cmd_logginger(message, log_type, text)
        await msg_default(message)

    # Проверка на ошибку и ее логирование
    except Exception as e:
        text_error = await error_cmd_logginger(message, log_type, e)
        return text_error
