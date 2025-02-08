# BotCode/routers/common/phrase.py
# Обработчик особых команд

from aiogram import Router, types, F
from aiogram.types import ReplyKeyboardRemove

from BotCode.routers.msg_default import *
from BotLibrary import find_imp_id, types_message, common_msg_logginger
from BotCode.keyboards.reply_kb.start_kb import ButtonText

# Настройка экспорта модулей и роутера
__all__ = ("router",)

router = Router(name="phrase_message_router")


# Ответ бота на кнопку или сообщение: "Привет!"
@router.message(F.text.lower() == ButtonText.Hello.lower())
async def hello_message(message: types.Message):
    log_type = "Start_Button"
    text_message = f"Привет, я бот. А ты кто?"
    name = find_imp_id(message.from_user.id)
    message_type = types_message(message)

    await message.reply(
        text=text_message,
    )

    await common_msg_logginger(message, name, message_type, log_type)
    await msg_default(message)


# Ответ бота на кнопку или сообщение: "Помощь!"
@router.message(F.text.lower() == ButtonText.Help.lower())
async def help_message(message: types.Message):
    log_type = "Help_Button"
    text_message = f"Привет, я надеюсь помогу тебе... Лучше напиши /help.."
    name = find_imp_id(message.from_user.id)
    message_type = types_message(message)

    await message.reply(
        text=text_message,
    )

    await common_msg_logginger(message, name, message_type, log_type)
    await msg_default(message)


# Ответ бота на кнопку или сообщение: "Пока-пока!"
@router.message(F.text.lower() == ButtonText.Bye.lower())
async def bye_message(message: types.Message):
    log_type = "Messages"
    text_message = f"Надеюсь скоро увидимся! Захочешь поговорить нажми на /start!"
    name = find_imp_id(message.from_user.id)
    message_type = types_message(message)

    await message.reply(
        text=text_message,
        reply_markup=ReplyKeyboardRemove(),
    )

    await common_msg_logginger(message, name, message_type, log_type)
    await msg_default(message)


# Ответ бота на сообщение: "Кошмар"
@router.message(F.text.lower() == "кошмар")
async def scary_message(message: types.Message):
    log_type = "Scary"
    text_message = f"Кошмар, тот еще!"
    name = find_imp_id(message.from_user.id)
    message_type = types_message(message)

    await message.reply(
        text=text_message,
    )

    await common_msg_logginger(message, name, message_type, log_type)
    await msg_default(message)
