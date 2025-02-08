# BotCode/keyboards/reply_kb/start_kb.py
# Создания клавиатуры на команду: /start
# Для создания базовой клавиатуры с некими элементами

from aiogram.types import ReplyKeyboardMarkup
from BotLibrary import rkb

# Настройка экспорта из этого модуля
__all__ = ("get_start_kb", "ButtonText")


# Создание класса со значениями кнопок
class ButtonText:
    Hello = "Привет!"
    Help = "Помогите!"
    Bye = "Пока-пока!"


# Функция создания клавиатуры на команду: /start
def get_start_kb() -> ReplyKeyboardMarkup:
    rkb.button(text=ButtonText.Hello)
    rkb.button(text=ButtonText.Help)
    rkb.button(text=ButtonText.Bye)
    rkb.adjust(2)
    return rkb.as_markup(resize_keyboard=True, one_time_keyboard=True)
