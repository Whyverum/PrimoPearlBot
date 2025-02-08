# BotCode/keyboards/reply_kb/survey_yesno_kb.py
# Создания клавиатуры на команду: /survey
# Для того, чтобы определить отправлять ли сообщения в будущем

from aiogram.types import ReplyKeyboardMarkup
from BotLibrary import rkb

# Настройка экспорта из этого модуля
__all__ = ("get_survey_email_kb", "ButtonText")


# Создание класса со значениями кнопок
class ButtonText:
    Yes = "Да"
    No = "Нет"


# Функция создания клавиатуры на команду: /survey
def get_survey_email_kb() -> ReplyKeyboardMarkup:
    rkb.button(text=ButtonText.Yes)
    rkb.button(text=ButtonText.No)
    rkb.adjust(1)
    return rkb.as_markup(resize_keyboard=True, one_time_keyboard=True)
