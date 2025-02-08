# BotCode/keyboards/reply_kb/more_kb.py
# Создания клавиатуры на команду: /more
# Для проверки отправки информации о пользователе

from aiogram.types import KeyboardButtonPollType, ReplyKeyboardMarkup
from BotLibrary import rkb

# Настройка экспорта из этого модуля
__all__ = ("get_more_kb", "ButtonText")


# Создание класса со значениями кнопок
class ButtonText:
    Location = "Отправить локацию"
    Contact = "Отправить контакт"
    Poll = "Отправить опрос"


# Функция создания клавиатуры на команду: /more
def get_more_kb() -> ReplyKeyboardMarkup:
    rkb.button(text=ButtonText.Location, request_location=True)
    rkb.button(text=ButtonText.Contact, request_contact=True)
    rkb.button(text=ButtonText.Poll, request_poll=KeyboardButtonPollType())
    rkb.adjust(1)
    return rkb.as_markup(resize_keyboard=True, one_time_keyboard=True)
