# bot_command.py

from aiogram import Router, types
from aiogram.filters import Command

from settings import *

from .user_cmd.start_cmd import type_messages as start_cmd_text
from .user_cmd.help_cmd import type_messages as help_cmd_text
from .user_cmd.exit_cmd import type_messages as exit_cmd_text

router = Router(name="bot_command_router")


# Хэндлер на команду /setcommands для использования в чате
@router.message(Command("setcommands", "setcommand", "ыуесщььфтвы", "ыуесщььфтв",
                        "setcmd", "setcmds", "ыуесьв", prefix=BotEdit.prefixs, ignore_case=True))
async def set_cmd_user(message: types.Message):
    # Проверка на admin ID
    if message.from_user.id not in ListId.adm_list_id:
        return f"Пользователей не в списке администраторов"
    await set_commands()
    return f"Команды успешно установлены!"


# Создаем команды в список бота
async def set_commands():
    bot_commands = [
        types.BotCommand(command=start_cmd_text.lower(), description="Запустить бота"),
        types.BotCommand(command=help_cmd_text.lower(), description="Получить помощь"),
        types.BotCommand(command=exit_cmd_text.lower(), description="Выйти из чата (в разработке)"),
        types.BotCommand(command="command", description="Пустая команда"),
    ]
    await bot.set_my_commands(bot_commands)
    return bot_commands
