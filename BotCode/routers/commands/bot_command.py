# BotCode/routers/commands/bot_command.py
# Работа с админ-командой /setcommands, для назначения команд
# Функция установки списка команд бота

from aiogram import Router, types, F
from aiogram.filters import Command
from BotLibrary import *

from .user_cmd.start_cmd import description as start_description, log_type as start_cmd
from .user_cmd.help_cmd import description as help_description, log_type as help_cmd
from .user_cmd.exit_cmd import description as exit_description, log_type as exit_cmd
from .user_cmd.start_time_cmd import description as start_time_description,log_type as start_time_cmd


# Создание роутера и настройка экспорта модулей
__all__ = ("router", "set_commands",)
router = Router(name="bot_command_router")
log_type = "SetCmd"

# Список ключевых слов для команды "setcommands"
secret_keywords = ["setcommands", "setcommand", "ыуесщььфтвы", "ыуесщььфтв",
                   "setcmd", "setcmds", "ыуесьв",]


# Хэндлер на команду /setcommands для использования в чате
@router.message(F.from_user.id.func(lambda user_id: str(user_id) in DataID.important.keys()),
                Command(*secret_keywords, prefix=BotVariables.prefixs, ignore_case=True))
@router.message(F.from_user.id.func(lambda user_id: str(user_id) in DataID.important.keys()),
                F.text.lower().in_(secret_keywords))
async def set_commands():
    bot_commands = [
        types.BotCommand(command=start_cmd.lower(), description=start_description),
        types.BotCommand(command=help_cmd.lower(), description=help_description),
        types.BotCommand(command=start_time_cmd.lower(), description=start_time_description),
        types.BotCommand(command=exit_cmd.lower(), description=exit_description),
    ]
    await bot.set_my_commands(bot_commands)
