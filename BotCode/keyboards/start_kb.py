# BotCode/keyboards/start_kb.py
# Создания клавиатуры на команду: /start

from aiogram import Router
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

# Создание роутера и настройка экспорта
__all__ = ("router", "get_start_kb", "kb_text", "ButtonText",)
kb_text = "StartKb"
router = Router(name="start_kb_router")


# Класс с названиями кнопок
class ButtonText:
    Hello = "Привет!"
    Help = "Помогите!"
    Bye = "Пока-пока!"


# Функция создания клавиатуры на команду: /start
def get_start_kb() -> ReplyKeyboardBuilder:
    button_hello = KeyboardButton(text=ButtonText.Hello)
    button_help = KeyboardButton(text=ButtonText.Help)
    button_bye = KeyboardButton(text=ButtonText.Bye)

    buttons_first_row = [button_hello, button_help]
    buttons_second_row = [button_bye]
    markup = ReplyKeyboardMarkup(
        keyboard=[buttons_first_row, buttons_second_row],
        resize_keyboard=True,
        one_time_keyboard=True,
    )
    return markup
