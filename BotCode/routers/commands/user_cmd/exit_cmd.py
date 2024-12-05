# BotCode/routers/commands/user_cmd/exit_cmd.py
# Работа с командой /exit, для покидания чата   (в разработке)

from aiogram import Router, types
from aiogram.filters import Command
from BotSettings import *

# Создание роутера и экспорта
__all__ = ("router", "command_text",)
router = Router(name="exit_router")
command_text = "Exit"


# Обработчик команды /exit
@router.message(Command("выход", "ds[j;", "exit", "учше", prefix=BotEdit.prefixs, ignore_case=True))
async def exit_cmd(message: types.Message):
    try:
        # Вывод сообщения пользователю и его блокировка
        text = f"Пользователь {message.from_user.id} успешно вышел из чата!"
        await message.reply(text)
        await bot.ban_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)

        # Активация логгера
        await cmd_logginger(message, command_text, text)

        return text

    # Проверка на ошибку и ее логирование
    except Exception as e:
        text_error = await error_cmd_logginger(message, command_text, e)
        return text_error
