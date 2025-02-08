# BotCode/keyboards/inline_kb/actor_kb.py
# Создания инлайн-клавиатуры на команду: /actor

from aiogram.types import InlineKeyboardMarkup
from BotLibrary import ikb

# Создание роутера и настройка экспорта
__all__ = ("get_actor_kb", "ButtonInl")


# Класс с параметрами кнопок
class ButtonInl:
    tg_chn = "Канал в тг!"
    tg_chn_url = "https://t.me/adeptusfiziks"

    tg_chat = "Чатик в тг)"
    tg_chat_url = "https://t.me/+T8mzbb_StRpiNDdi"

    web_text = "Веселая игра скачать"
    web_url = "https://gamejolt.com/games/UndertaleYellow/136925"

    random_site = "Рандомный сайт"
    random_site_cbd = "random_site_cbd"

    random_num_dice = "Рандомное число"
    random_num_dice_cbd = "random_num_dice_cbd"

    random_num_modal = "Рандомный виджет"
    random_num_modal_cdb = "random_num_modal_cdb"



# Функция создания клавиатуры на команду: /actor
def get_actor_kb() -> InlineKeyboardMarkup:
    # Добавляем кнопки, группируя их по строкам
    ikb.button(text=ButtonInl.tg_chn, url=ButtonInl.tg_chn_url)
    ikb.button(text=ButtonInl.tg_chat, url=ButtonInl.tg_chat_url)

    ikb.button(text=ButtonInl.web_text, url=ButtonInl.web_url)
    ikb.button(text=ButtonInl.random_site, callback_data=ButtonInl.random_site_cbd)
    ikb.button(text=ButtonInl.random_num_dice, callback_data=ButtonInl.random_num_dice_cbd)
    ikb.button(text=ButtonInl.random_num_modal, callback_data=ButtonInl.random_num_modal_cdb)

    ikb.adjust(2, 1)
    return ikb.as_markup()
