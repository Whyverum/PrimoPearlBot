# BotCode/routers/common/messages.py   (Разберись с логгированием!!!!!)
# Нижний обработчик всех текстовых сообщений
# А также нескольких определенных сообщений (Перенести в иной файл!!!)

from BotSettings import *
from aiogram import Router, types, F
from aiogram.types import ReplyKeyboardRemove

from BotCode.keyboards.start_kb import ButtonText
from ..downloads.download_avatar_all import download_avatar

# Настройка экспорта модулей и роутера
__all__ = ("router",)
router = Router(name="common_message_router")
type_messages = "Messages"


# Ответ бота на кнопку или сообщение: "Привет!"
@router.message(F.text.lower() == ButtonText.Hello.lower())
async def bye(message: types.Message):
    type_messages = "Start_Button"
    text_message = f"Привет, я бот. А ты кто?"
    await message.reply(
        text=text_message,
    )
    # logger.bind(custom_variable=type_messages, user_var=str(message.from_user.username)).info(
    #     f"Получено сообщение из ({name}) : {message_type}")
    return text_message


# Ответ бота на кнопку или сообщение: "Помощь!"
@router.message(F.text.lower() == ButtonText.Help.lower())
async def help_message(message: types.Message):
    type_messages = "Help_Button"
    text_message = f"Привет, я надеюсь помогу тебе... Лучше напиши /help.."
    await message.reply(
        text=text_message,
    )
    return text_message


# Ответ бота на кнопку или сообщение: "Пока-пока!"
@router.message(F.text.lower() == ButtonText.Bye.lower())
async def bye_message(message: types.Message):
    text_message = f"Надеюсь скоро увидимся! Захочешь поговорить нажми на /start!"
    await message.reply(
        text=text_message,
        reply_markup=ReplyKeyboardRemove(),
    )
    return text_message


# Ответ бота на сообщение: "Кошмар"
@router.message(F.text.lower() == "кошмар")
async def scary_message(message: types.Message):
    text_message = f"Кошмар, тот еще!"
    await message.reply(
        text=text_message,
    )
    return text_message


# Хэндлер на все сообщения и записывает данные
@router.message()
async def handle_all_messages(message: types.Message):
    name = find_chat_id(message)
    await logginger(message)
    await download_avatar(message)
    message_type = types_message(message)

    # Проверка на наличие текста и его типа
    if message.text is None:
        logger.bind(custom_variable=type_messages, user_var=f"@{message.from_user.username}").info(
            f"Получено сообщение из ({name}) : {message_type}")
    else:
        logger.bind(custom_variable=type_messages, user_var=f"@{message.from_user.username}").info(
            f"Получено сообщение из ({name}) : {message.text}")

    return f"Получено новое сообщение!"
