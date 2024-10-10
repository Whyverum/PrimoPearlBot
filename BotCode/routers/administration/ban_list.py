# ban_list.py

from loguru import logger
from aiogram import Router, types

from BotCode import config
from BotCode.routers.administration.analitics_handlers import loginger

router = Router(name=__name__)


# Хэндлер на все сообщения + сообщение Кошмар. Он и записывает данные
@router.message(lambda message: message.from_user.id in config.ban_list_id)
async def banned_user(message: types.Message):
    name = message.chat.id
    if name in config.important_ids:
        name = config.important_ids[name]
    await loginger(message)
    logger.bind(custom_variable="BAN", user_var=str(message.from_user.username)).info(
        f"Получено сообщение от забанненго пользователя из ({name}) : {message.text}")
    await message.answer("Вы были забаннены!")
