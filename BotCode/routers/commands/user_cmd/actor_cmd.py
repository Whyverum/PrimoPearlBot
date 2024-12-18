# BotCode/routers/commands/user_cmd/actor_cmd.py
# разработка

from aiogram import Router, types, F
from aiogram.filters import Command
from BotLibrary import *
from keyboards.inline_kb.actor_kb import get_actor_kb

# Создание роутера и настройка экспорта модулей
__all__ = ("router", "cmd_actor", "log_type",)
router = Router(name="actor_router")
log_type = "Actor"


# Список ключевых слов для команды
keywords = ["actor", "фсещк",]


# Обработчик команды /actor
@router.message(Command(*keywords, prefix=BotEdit.prefixs, ignore_case=True))
@router.message(F.text.lower().in_(keywords))
async def cmd_actor(message: types.Message):
    try:
        # Вывод сообщения пользователю
        text = f"использовал(а) команду /{log_type.lower()}"
        markup = get_actor_kb()

        await message.reply(
            text="Всякое разное для тебя",
            reply_markup=markup,
        )


        # Активация логгера
        await cmd_logginger(message, log_type, text)
        return text

    # Проверка на ошибку и ее логирование
    except Exception as e:
        text_error = await error_cmd_logginger(message, log_type, e)
        return text_error
