# BotCode/routers/commands/bot_command.py
# Работа с админ-командой /setcommands, для назначения команд
# Функция установки списка команд бота

from aiogram import Router, types
from aiogram.filters import Command
from BotSettings import BotEdit, find_adm_id, bot

from .user_cmd.start_cmd import command_text as start_cmd_text
from .user_cmd.help_cmd import command_text as help_cmd_text
from .user_cmd.exit_cmd import command_text as exit_cmd_text

# Создание роутера и настройка экспорта
__all__ = ("router", "set_cmd_user", "set_commands", "command_text",)
command_text = "SetCmd"
router = Router(name="bot_command_router")


# Хэндлер на команду /setcommands для использования в чате
@router.message(Command("setcommands", "setcommand", "ыуесщььфтвы", "ыуесщььфтв",
                        "setcmd", "setcmds", "ыуесьв", prefix=BotEdit.prefixs, ignore_case=True))
async def set_cmd_user(message: types.Message):
    # Проверка на admin ID
    text = find_adm_id(message)
    if text:
        await set_commands()
        return f"Команды успешно установлены!"
    else:
        await message.reply(text)
        return text


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
