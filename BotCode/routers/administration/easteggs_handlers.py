# BotCode/routers/administration/easteggs_handlers.py
# Небольшие шуточные пасхалки

from aiogram import Router, types, F
from aiogram.enums import ChatAction
from BotLibrary import *
from routers.msg_default import msg_default

# Создание роутера и настройка экспорта
__all__ = ("router",)
router = Router(name="easteggs_router")
log_type = "EastEggs"


# Хэндлер на текст финаки228
@router.message(F.text.lower() == "финаки228")
async def secret_admin_message_finaki(message: types.Message):
    text = "Пасхалка 1 Финаки228 найдена!"

    # Отправка действия "печатает"
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.TYPING,
    )

    # Отправка фотографии
    try:
        await message.reply_photo(
            photo=types.FSInputFile(path=f"{ProjectPath.personal_media}/{ProjectPath.personal_photo}/Undertale.jpg"),
            caption="ОНА МЕНЯ ЗАСТАВИЛА ПОМОГИТЕ😭... (Кст @fin_aki любит анал, тс..)",
        )

    # Проверка на ошибку и ее логирование
    except Exception as e:
        logger.error(f"Ошибка при отправке фото: {e}")
        await message.answer("Не удалось отправить фото, проверьте настройки пути или файл.")

    # Дополнительное логирование
    await cmd_logginger(message, log_type, text)
    await msg_default(message)


# Хэндлер на текст финикх
@router.message(F.from_user.id.func(lambda user_id: str(user_id) in DataID.important.keys()),
                F.text.lower() == "финикх")
async def secret_admin_message_finik(message: types.Message):
    text = f"Пасхалка 2 финикx найдена!"
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.UPLOAD_PHOTO,
    )
    await message.answer_photo(
        photo="https://vos-mo.ru/upload/iblock/329/g0s939ge8o1n8xp7rcqnw9kkz9mcfrg2/risunok.jpg",
        caption="Привет, это польза Фиников!")
    await cmd_logginger(message, log_type, text)
    await msg_default(message)


# Хэндлер на текст андертейлкино
@router.message(F.text.lower() == "андертейлкино")
async def secret_admin_message_finik(message: types.Message):
    text = f"Пасхалка 3 андертейлкино найдена!"
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.UPLOAD_PHOTO,
    )
    await message.answer_photo(
        photo="https://i.ytimg.com/vi/c-o4_p4YKIc/mqdefault.jpg",
        caption="Меня заставила Финаки, честно!")
    await cmd_logginger(message, log_type, text)
    await msg_default(message)


# Хэндлер на текст ришкус + отправка с локального хранилища
@router.message(F.text.lower() == "ришкус")
async def secret_admin_message_rishkus(message: types.Message):
    text = f"Пасхалка 4 ришкус найдена!"
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.UPLOAD_PHOTO,
    )
    await message.reply_photo(
        photo=types.FSInputFile(path=f"{ProjectPath.personal_media}/{ProjectPath.personal_photo}/Кусь.jpg"),
        caption="Россия для грустных",
    )
    await cmd_logginger(message, log_type, text)
    await msg_default(message)


# Хэндлер на текст skodavano + отправка с локального хранилища
@router.message(F.text.lower() == "skodavano")
async def secret_admin_message_skodavano(message: types.Message):
    text = f"Пасхалка 5 skodavano найдена!"
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.UPLOAD_PHOTO,
    )
    await message.reply_photo(
        photo=types.FSInputFile(path=f"{ProjectPath.personal_media}/{ProjectPath.personal_photo}/Vano.jpg"),
        caption="SkodaRacingVano24 -> Синяя изолента",
    )
    await cmd_logginger(message, log_type, text)
    await msg_default(message)


# Хэндлер на текст лостикслешик + отправка с локального хранилища
@router.message(F.text.lower() == "лостикслешик")
async def secret_admin_message_lostik(message: types.Message):
    try:
        text = f"Пасхалка 6 лостикслешик найдена!"
        logger.bind(log_type=log_type, user=message.from_user.username).info(text)
        # Отправка статуса отправки гифки
        await message.bot.send_chat_action(
            chat_id=message.chat.id,
            action=ChatAction.UPLOAD_VIDEO
        )

        # Вывод сообщения-гифки пользователю
        await message.reply_animation(
            animation=types.FSInputFile(path=f"{ProjectPath.personal_media}"
                                             f"/{ProjectPath.personal_gif}/ЛжеРайяПрайм.mp4")
        )

        # Активация логгера
        await cmd_logginger(message, types_message, text)
        await msg_default(message)

    # Проверка на ошибку и ее логирование
    except Exception as e:
        text_error = await error_cmd_logginger(message, log_type, e)
        return text_error


# Хэндлер на текст ещкере
@router.message(F.text.lower() == "ещкере")
async def secret_admin_message_finaki(message: types.Message):
    text = "Пасхалка 7 ещкере найдена!"

    # Отправка действия "печатает"
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.TYPING,
    )

    # Логгирование с дополнительными переменными
    logger.bind(log_type=log_type, user=message.from_user.username).info(text)

    # Отправка фотографии
    try:
        await message.reply_photo(
            photo="https://t2.genius.com/unsafe/1249x0/https%3A%2F%2Fimages"
                  ".genius.com%2Fb7b22809fa5a38a3bbf861abb2a74b87.400x400x1.jpg",
            caption="ЕЩКЕРЕ " * 50)

    # Проверка на ошибку и ее логирование
    except Exception as e:
        error_text = f"Ошибка при отправке фото: {e}"
        logger.bind(log_type=log_type, user=message.from_user.username).error(error_text)
        await message.answer("Не удалось отправить фото, проверьте настройки пути или файл.")

    # Дополнительное логирование
    await cmd_logginger(message, log_type, text)
    await msg_default(message)


# Хэндлер на текст маз
@router.message(F.text.lower() == "маз")
async def secret_admin_message_finaki(message: types.Message):
    text = "Пасхалка 8 маз найдена!"

    # Отправка действия "загружает видео"
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.UPLOAD_VIDEO,  # Действие изменено на загрузку видео
    )

    # Логирование с дополнительными переменными
    logger.bind(log_type=log_type, user=message.from_user.username).info(text)

    # Отправка видео
    try:
        await message.reply(text="[ФИНАКИ+МАЗЕЛОВ=ЛЮБОВЬ](https://www.youtube.com/watch?v=st3avf3QZ1w)",
                            parse_mode="Markdown")

    # Проверка на ошибку и её логирование
    except Exception as e:
        error_text = f"Ошибка при отправке видео: {e}"
        logger.bind(log_type=log_type, user=message.from_user.username).error(error_text)
        await message.answer("Не удалось отправить видео, проверьте настройки пути или файл.")

    # Дополнительное логирование
    await cmd_logginger(message, log_type, text)
    await msg_default(message)
