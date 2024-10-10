# common.py

from aiogram import Router, types
from loguru import logger
from BotCode.routers.administration.analitics_handlers import loginger
from BotCode import config


router = Router(name=__name__)


# Хэндлер на все сообщения + сообщение Кошмар. Он и записывает данные
@router.message()
async def handle_all_messages(message: types.Message):
    await loginger(message)
    name = message.chat.id
    expression = message.text

    if name in config.important_ids:
        name = config.important_ids[name]
    logger.bind(custom_variable="Messages", user_var=str(message.from_user.username)).info(
        f"Получено сообщение из ({name}) : {message.text}")

    # if any(char.isdigit() for char in expression):
    #     try:
    #         result = eval(expression)
    #         await message.answer(f"{expression} = {result}")
    #     except Exception as e:
    #         await message.answer(f"Ошибка: {e}")

    if message.text and message.text.lower() == "кошмар":
        await message.answer("Кошмар, тот еще!")
