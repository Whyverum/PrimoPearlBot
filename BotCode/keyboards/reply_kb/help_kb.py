# BotCode/keyboards/reply_kb/help_kb.py
# Создание клавиатуры для сообщения: "Помогите!"
# Создает небольшую числовую клавиатуру для тестов

from aiogram import Router, F
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from BotLibrary import rkb

# Создание роутера и настройка экспорта модулей
__all__ = ("router", "get_help_kb")
router = Router(name="help_kb_router")


# Функция создания клавиатуры на сообщение: "Помогите!"
@router.message(F.text.lower() == "помогите!")
def get_help_kb() -> ReplyKeyboardMarkup:
    numbers = [
        "1️⃣", "2️⃣", "3️⃣",
        "4️⃣", "5️⃣", "6️⃣",
        "7️⃣", "8️⃣", "9️⃣",
            "0️⃣",
    ]

    # Создание кнопки каждого числа по отдельности
    buttons_row = [KeyboardButton(text=num) for num in numbers]
    for num in numbers:
        rkb.button(text=num)

    rkb.adjust(3)
    return rkb.as_markup(resize_keyboard=True)
