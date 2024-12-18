# BotCode/routers/commands/bot_command.py
# Работа с админ-командой /setcommands, для назначения команд
# Функция установки списка команд бота

from aiogram import Router, types, F
from aiogram.filters import Command
from BotLibrary import *

from .user_cmd.start_cmd import log_type as start_cmd_text
from .user_cmd.help_cmd import log_type as help_cmd_text
from .user_cmd.exit_cmd import log_type as exit_cmd_text
from .user_cmd.start_time_cmd import log_type as start_time_cmd_text


# Создание роутера и настройка экспорта модулей
__all__ = ("router", "set_commands",)
router = Router(name="bot_command_router")
log_type = "SetCmd"

# Список ключевых слов для команды "setcommands"
secret_keywords = ["setcommands", "setcommand", "ыуесщььфтвы", "ыуесщььфтв",
                   "setcmd", "setcmds", "ыуесьв",]


# Хэндлер на команду /setcommands для использования в чате
@router.message(F.from_user.id.in_(ListId.important_ids),
                Command(*secret_keywords, prefix=BotEdit.prefixs, ignore_case=True))
async def set_commands():
    bot_commands = [
        types.BotCommand(command=start_cmd_text.lower(), description="Запустить бота"),
        types.BotCommand(command=help_cmd_text.lower(), description="Получить помощь"),
        types.BotCommand(command=help_cmd_text.lower(), description="Получить помощь"),
        types.BotCommand(command=start_time_cmd_text.lower(), description="Время запуска"),
        types.BotCommand(command=exit_cmd_text.lower(), description="Выйти из чата (в разработке)"),
        types.BotCommand(command="command", description="Пустая команда"),
    ]
    await bot.set_my_commands(bot_commands)
    return bot_commands
