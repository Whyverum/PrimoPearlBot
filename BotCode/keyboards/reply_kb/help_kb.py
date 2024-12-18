# BotCode/keyboards/help_kb.py
# Создание клавиатуры для сообщения: "Помогите!"

from aiogram import Router, F
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

# Создание роутера и настройка экспорта модулей
__all__ = ("router", "get_help_kb", "kb_text",)
kb_text = "HelpKb"
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

    buttons_row = [KeyboardButton(text=num) for num in numbers]
    # Один из способов создания клавиатур

    #
    # markup = ReplyKeyboardMarkup(
    #     keyboard=[buttons_row],
    #     resize_keyboard=True,
    # )
    # return markup

    builder = ReplyKeyboardBuilder()
    for num in numbers:
        builder.button(text=num)
    builder.adjust(3)
    builder.row(buttons_row[3], buttons_row[9])
    builder.add(buttons_row[-1])

    return builder.as_markup(resize_keyboard=True)
