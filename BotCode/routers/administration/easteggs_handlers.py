# easteggs_handlers.py

from aiogram import Router, types, F
from aiogram.enums import ChatAction
from settings import *

router = Router(name="easteggs_router")
type_messages = "EastEggs"


# Хэндлер на текст финаки228
@router.message(F.text.lower() == "финаки228")
async def secret_admin_message_finaki(message: types.Message):
    text = f"Пасхалка 1 Финаки228 найдена!"
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.TYPING,
    )
    logger.bind(custom_variable=type_messages, user_var=str(message.from_user.username)).info(text)
    await message.reply("Она кстати любит анал")
    await logginger(message)
    return text


# Хэндлер на текст финик
@router.message(F.from_user.id.in_(ListId.important_ids), F.text.lower() == "финикх")
async def secret_admin_message_finik(message: types.Message):
    text = f"Пасхалка 2 финикx найдена!"
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.UPLOAD_PHOTO,
    )
    logger.bind(custom_variable=type_messages, user_var=str(message.from_user.username)).info(text)

    await message.answer_photo(
        photo="https://vos-mo.ru/upload/iblock/329/g0s939ge8o1n8xp7rcqnw9kkz9mcfrg2/risunok.jpg",
        caption="Привет, это польза Фиников!")
    await logginger(message)
    return text


# Хэндлер на текст финик
@router.message(F.text.lower() == "андертейлкино")
async def secret_admin_message_finik(message: types.Message):
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.UPLOAD_PHOTO,
    )
    logger.bind(custom_variable=type_messages, user_var=str(message.from_user.username)).info(
        "Пасхалка 3 андертейлкино найдена!")
    await message.answer_photo(
        photo="https://i.ytimg.com/vi/c-o4_p4YKIc/mqdefault.jpg",
        caption="Меня заставила Финаки, честно!")
    await logginger(message)


# Хэндлер на текст ришкус + отправка с локального хранилища
@router.message(F.text.lower() == "ришкус")
async def secret_admin_message_rishkus(message: types.Message):
    text = f"Пасхалка 4 ришкус найдена!"
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.UPLOAD_PHOTO,
    )
    logger.bind(custom_variable=type_messages, user_var=str(message.from_user.username)).info(text)
    await message.reply_photo(
        photo=types.FSInputFile(path="BotFiles/BotMedia/MediaPersonal/Photo/Кусь.jpg"),
        caption="Россия для грустных",
    )
    await logginger(message)
    return text


# Хэндлер на текст skodavano + отправка с локального хранилища
@router.message(F.text.lower() == "skodavano")
async def secret_admin_message_rishkus(message: types.Message):
    text = f"Пасхалка 5 skodavano найдена!"
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.UPLOAD_PHOTO,
    )
    logger.bind(custom_variable=type_messages, user_var=str(message.from_user.username)).info(text)
    await message.reply_photo(
        photo=types.FSInputFile(path="BotFiles/BotMedia/MediaPersonal/Photo/Vano.jpg"),
        caption="SkodaRacingVano24 -> Синяя изолента",
    )
    await logginger(message)
    return text


# Хэндлер на текст лостикслешик + отправка с локального хранилища
@router.message(F.text.lower() == "лостикслешик")
async def secret_admin_message_lostik(message: types.Message):
    text = f"Пасхалка 6 лостикслешик найдена!"
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.UPLOAD_VIDEO
    )
    logger.bind(custom_variable=type_messages, user_var=str(message.from_user.username)).info(text)
    await message.reply_animation(
        animation=types.FSInputFile(path="BotFiles/BotMedia/MediaPersonal/GIF/ЛжеРайяПрайм.mp4"),
    )
    await logginger(message)
    return text
