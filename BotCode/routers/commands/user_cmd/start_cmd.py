# start_cmd.py

from aiogram import Router, types
from aiogram.filters import Command
from settings import *
from BotCode.keyboards.start_kb import get_start_kb

router = Router(name="start_router")
type_messages = "Start"


# Хэндлер на команду /start или /старт
@router.message(Command("start", "старт", "запуск", "пуск", "on", "вкл", "с", "s", "ы",
                    "ыефке", "cnfhn", "pfgecr", "gecr", prefix=BotEdit.prefixs, ignore_case=True))
async def cmd_start(message: types.Message):
    await logginger(message)
    try:
        text = f"Команда /start активирована"
        await message.reply(text=f"Стартовый бот!", reply_markup=get_start_kb())
        logger.bind(custom_variable=type_messages, user_var=str(message.from_user.username)).info(text)
        return text

    # Проверка на ошибку и ее логирование   (В разработке)
    except Exception as e:
        text_error = f"Ошибка при использовании команды /{type_messages.lower()}: {str(e)}\n"
        setup_error_logger()
        logger.bind(custom_variable=type_messages, user_var=f"@{message.from_user.username}").error(text_error)
        setup_logger()
        return text_error
