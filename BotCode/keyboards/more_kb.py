# BotCode/keyboards/more_kb.py
# Создания клавиатуры на команду: /more

from aiogram import Router
from aiogram.types import KeyboardButtonPollType
from aiogram.utils.keyboard import ReplyKeyboardBuilder

# Создание роутера и настройка экспорта модулей
__all__ = ("router", "get_more_kb", "kb_text",)
kb_text = "HelpKb"
router = Router(name="more_kb_router")


# Класс с названиями кнопок
class ButtonText:
    More = "More"
    Location = "Отправить локацию"
    Contact = "Отправить контакт"
    Chat = "Отправить чат???"
    Poll = "Отправить опрос"
    Users = "Что то с common"


# Функция создания клавиатуры на команду: /more
def get_more_kb() -> ReplyKeyboardBuilder:
    builder = ReplyKeyboardBuilder()
    # builder.add(KeyboardButton(text=ButtonText.Location, request_location=True))
    builder.button(text=ButtonText.Location, request_location=True)
    builder.button(text=ButtonText.Contact, request_contact=True)
    builder.button(text=ButtonText.Poll, request_poll=KeyboardButtonPollType())

    builder.adjust(1)
    return builder.as_markup(resize_keyboard=True)

    # Один из вариантов создание клавиатуры
    # markup = ReplyKeyboardMarkup(
    #     keyboard=[]
    # )
    # return markup
