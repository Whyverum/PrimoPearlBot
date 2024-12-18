# BotCode/routers/common/messages.py   (Разберись с логгированием!!!!!)
# Нижний обработчик всех текстовых сообщений
# А также нескольких определенных сообщений (Перенести в иной файл!!!)

from BotLibrary import *
from aiogram import Router, types, F
from aiogram.types import ReplyKeyboardRemove

from BotCode.keyboards.start_kb import ButtonText
from ..downloads.download_avatar_all import download_avatar

# Настройка экспорта модулей и роутера
__all__ = ("router",)
router = Router(name="common_message_router")


# Ответ бота на кнопку или сообщение: "Привет!"
@router.message(F.text.lower() == ButtonText.Hello.lower())
async def bye(message: types.Message):
    log_type = "Start_Button"
    text_message = f"Привет, я бот. А ты кто?"
    name = find_chat_id(message)
    message_type = types_message(message)

    await message.reply(
        text=text_message,
    )

    await common_msg_logginger(message, name, message_type, log_type)
    return text_message


# Ответ бота на кнопку или сообщение: "Помощь!"
@router.message(F.text.lower() == ButtonText.Help.lower())
async def help_message(message: types.Message):
    log_type = "Help_Button"
    text_message = f"Привет, я надеюсь помогу тебе... Лучше напиши /help.."
    name = find_chat_id(message)
    message_type = types_message(message)

    await message.reply(
        text=text_message,
    )

    await common_msg_logginger(message, name, message_type, log_type)
    return text_message


# Ответ бота на кнопку или сообщение: "Пока-пока!"
@router.message(F.text.lower() == ButtonText.Bye.lower())
async def bye_message(message: types.Message):
    log_type = "Messages"
    text_message = f"Надеюсь скоро увидимся! Захочешь поговорить нажми на /start!"
    name = find_chat_id(message)
    message_type = types_message(message)

    await message.reply(
        text=text_message,
        reply_markup=ReplyKeyboardRemove(),
    )

    await common_msg_logginger(message, name, message_type, log_type)
    return text_message


# Ответ бота на сообщение: "Кошмар"
@router.message(F.text.lower() == "кошмар")
async def scary_message(message: types.Message):
    log_type = "Messages"
    text_message = f"Кошмар, тот еще!"
    name = find_chat_id(message)
    message_type = types_message(message)

    await message.reply(
        text=text_message,
    )

    await common_msg_logginger(message, name, message_type, log_type)
    return text_message


# Хэндлер на все сообщения и записывает данные
@router.message()
async def handle_all_messages(message: types.Message):
    log_type = "Messages"
    name = find_chat_id(message)
    message_type = types_message(message)

    await logginger(message)
    await download_avatar(message)

    await common_msg_logginger(message, name, message_type, log_type)
    return f"Получено новое сообщение!"
