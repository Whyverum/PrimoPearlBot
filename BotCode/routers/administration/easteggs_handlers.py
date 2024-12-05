# BotCode/routers/administration/easteggs_handlers.py
# Функции с шуточными пасхалками  (разобраться с логированием и ошибками)

from aiogram import Router, types, F
from aiogram.enums import ChatAction
from BotSettings import *


# Создание роутера и настройка экспорта
__all__ = ("router", "secret_admin_message_finaki", "secret_admin_message_lostik",
           "secret_admin_message_rishkus", "secret_admin_message_finik", "secret_admin_message_skodavano",)
router = Router(name="easteggs_router")
type_messages = "EastEggs"


# Хэндлер на текст финаки228
@router.message(F.text.lower() == "финаки228")
async def secret_admin_message_finaki(message: types.Message):
    text = "Пасхалка 1 Финаки228 найдена!"

    # Отправка действия "печатает"
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.TYPING,
    )

    # Логгирование с дополнительными переменными
    logger.bind(
        custom_variable="text_message",
        user_var=message.from_user.username
    ).info(text)

    # Отправка фотографии
    try:
        await message.reply_photo(
            photo=types.FSInputFile(path=f"{ImportantPath.bot_personal_media}/{ImportantPath.photo}/Undertale.jpg"),
            caption="ОНА МЕНЯ ЗАСТАВИЛА ПОМОГИТЕ😭... (Кст @fin_aki любит анал, тс..)",
        )

    # Проверка на ошибку и ее логирование
    except Exception as e:
        logger.error(f"Ошибка при отправке фото: {e}")
        await message.answer("Не удалось отправить фото, проверьте настройки пути или файл.")

    # Дополнительное логирование
    await logginger(message)
    return text


# Хэндлер на текст финикх
@router.message(F.from_user.id.in_(ListId.important_ids), F.text.lower() == "финикх")
async def secret_admin_message_finik(message: types.Message):
    text = f"Пасхалка 2 финикx найдена!"
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.UPLOAD_PHOTO,
    )
    logger.bind(custom_variable=type_messages, user_var=f"{message.from_user.username}").info(text)

    await message.answer_photo(
        photo="https://vos-mo.ru/upload/iblock/329/g0s939ge8o1n8xp7rcqnw9kkz9mcfrg2/risunok.jpg",
        caption="Привет, это польза Фиников!")
    await logginger(message)
    return text


# Хэндлер на текст андертейлкино
@router.message(F.text.lower() == "андертейлкино")
async def secret_admin_message_finik(message: types.Message):
    text = f"Пасхалка 3 андертейлкино найдена!"
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.UPLOAD_PHOTO,
    )
    logger.bind(custom_variable=type_messages, user_var=f"{message.from_user.username}").info(text)
    await message.answer_photo(
        photo="https://i.ytimg.com/vi/c-o4_p4YKIc/mqdefault.jpg",
        caption="Меня заставила Финаки, честно!")
    await logginger(message)
    return text


# Хэндлер на текст ришкус + отправка с локального хранилища
@router.message(F.text.lower() == "ришкус")
async def secret_admin_message_rishkus(message: types.Message):
    text = f"Пасхалка 4 ришкус найдена!"
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.UPLOAD_PHOTO,
    )
    logger.bind(custom_variable=type_messages, user_var=f"{message.from_user.username}").info(text)
    await message.reply_photo(
        photo=types.FSInputFile(path=f"{ImportantPath.bot_personal_media}/{ImportantPath.photo}/Кусь.jpg"),
        caption="Россия для грустных",
    )
    await logginger(message)
    return text


# Хэндлер на текст skodavano + отправка с локального хранилища
@router.message(F.text.lower() == "skodavano")
async def secret_admin_message_skodavano(message: types.Message):
    text = f"Пасхалка 5 skodavano найдена!"
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.UPLOAD_PHOTO,
    )
    logger.bind(custom_variable=type_messages, user_var=f"{message.from_user.username}").info(text)
    await message.reply_photo(
        photo=types.FSInputFile(path=f"{ImportantPath.bot_personal_media}/{ImportantPath.photo}/Vano.jpg"),
        caption="SkodaRacingVano24 -> Синяя изолента",
    )
    await logginger(message)
    return text


# Хэндлер на текст лостикслешик + отправка с локального хранилища
@router.message(F.text.lower() == "лостикслешик")
async def secret_admin_message_lostik(message: types.Message):
    try:
        text = f"Пасхалка 6 лостикслешик найдена!"

        # Отправка статуса отправки гифки
        await message.bot.send_chat_action(
            chat_id=message.chat.id,
            action=ChatAction.UPLOAD_VIDEO
        )

        # Вывод сообщения-гифки пользователю
        await message.reply_animation(
            animation=types.FSInputFile(path=f"{ImportantPath.bot_personal_media}/{ImportantPath.gif}/ЛжеРайяПрайм.mp4"),
        )

        # Активация логгера
        await cmd_logginger(message, types_message, text)
        return text

    # Проверка на ошибку и ее логирование
    except Exception as e:
        text_error = await error_cmd_logginger(message, type_messages, e)
        return text_error
