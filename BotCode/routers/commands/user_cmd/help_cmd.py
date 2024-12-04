# help_cmd.py

from aiogram import Router, types
from aiogram.filters import Command
from settings import *
from BotCode.keyboards.help_kb import get_help_kb

# Создание роутера "help_router"
router = Router(name="help_router")
type_messages = "Help"


# Хэндлер на команду /info или /help
@router.message(Command("help", "info", "помощь", "инфо", "?", "информация", "рудз", "штащ", "byaj",
                    "gjvjom", "byajhvfwbz", prefix=BotEdit.prefixs, ignore_case=True))
async def cmd_help(message: types.Message):
    try:
        text = f"Команда /help активирована"
        logger.bind(custom_variable=type_messages, user_var=str(message.from_user.username)).info(text)
        await message.answer(
            text=f"Ну это типо привет. Ладно, это помощь.",
            reply_markup=get_help_kb(),
            )
        await logginger(message)
        return text

    # Проверка на ошибку и ее логирование   (В разработке)
    except Exception as e:
        text_error = f"Ошибка при использовании команды /{type_messages.lower()}: {str(e)}\n"
        await setup_error_logger()
        logger.bind(custom_variable=type_messages, user_var=f"@{message.from_user.username}").error(text_error)
        await setup_logger()
        return text_error
