# BotCode/keyboards/start_kb.py
# Создания клавиатуры на команду: /start

from aiogram import Router
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

# Создание роутера и настройка экспорта
__all__ = ("router", "get_randnum_kb", "kb_text", "ButtonInl",)
kb_text = "RandNumKb"
router = Router(name="actor_kb_router")


# Класс с параметрами кнопок
class ButtonInl:
    mark_cbd = "mark_cbd"


# Функция создания клавиатуры на команду: /actor
def get_randnum_kb(text_msg="Получить ответ") -> InlineKeyboardMarkup:
    # Создаем билдер клавиатуры
    builder = InlineKeyboardBuilder()

    # Добавляем кнопки, группируя их по строкам
    builder.button(text=text_msg, callback_data=ButtonInl.mark_cbd)

    return builder.as_markup()
