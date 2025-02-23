# BotCode/keyboards/inline_kb/randnum_kb.py
# Создания инлайн-клавиатуры на команду: /randnum

from aiogram.types import InlineKeyboardMarkup
from BotLibrary import ikb

# Создание роутера и настройка экспорта
__all__ = ("get_randnum_kb", "ButtonInl")


# Класс с параметрами кнопок
class ButtonInl:
    text = "Получить ответ"
    mark_cbd = "mark_cbd"


# Функция создания клавиатуры на команду: /randnum
def get_randnum_kb(text=ButtonInl.text) -> InlineKeyboardMarkup:
    ikb.button(text=text, callback_data=ButtonInl.mark_cbd)
    ikb.adjust(1)
    return ikb.as_markup()  # Возвращаем клавиатуру

