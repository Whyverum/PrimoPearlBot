# easteggs_handlers.py

from aiogram import Router, F, types
from loguru import logger

from BotCode import config
from BotCode.routers.administration.analitics_handlers import loginger

router = Router(name=__name__)


# Хэндлер на текст финаки228
@router.message(F.from_user.id.in_(config.important_ids), F.text.lower() == "финаки228")
async def secret_admin_message_finaki(message: types.Message):
    logger.bind(custom_variable="EastEggs", user_var=str(message.from_user.username)).info("Пасхалка 1 Финаки228 найдена!")
    await message.reply("Она кстати любит анал")
    await loginger(message)


# Хэндлер на текст финик
@router.message(F.from_user.id.in_(config.important_ids), F.text.lower() == "финикх")
async def secret_admin_message_finik(message: types.Message):
    logger.bind(custom_variable="EastEggs", user_var=str(message.from_user.username)).info("Пасхалка 2 финикx найдена!")
    await message.answer_photo(
        photo="https://vos-mo.ru/upload/iblock/329/g0s939ge8o1n8xp7rcqnw9kkz9mcfrg2/risunok.jpg",
        caption="Привет, это польза Фиников!")
    await loginger(message)


# Хэндлер на текст финик
@router.message(F.from_user.id.in_(config.important_ids), F.text.lower() == "андертейлкино")
async def secret_admin_message_finik(message: types.Message):
    logger.bind(custom_variable="EastEggs", user_var=str(message.from_user.username)).info("Пасхалка 3 андертейлкино найдена!")
    await message.answer_photo(
        photo="https://i.ytimg.com/vi/c-o4_p4YKIc/mqdefault.jpg",
        caption="Меня заставила Финаки, честно!")
    await loginger(message)
