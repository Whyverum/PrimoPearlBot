# BotCode/keyboards/inline_kb/actor_kb.py
# Создания инлайн-клавиатуры на команду: /actor

from aiogram import Router
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

# Создание роутера и настройка экспорта
__all__ = ("router", "get_actor_kb", "kb_text", "ButtonInl",)
kb_text = "ActorKb"
router = Router(name="actor_kb_router")


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
    # Создаем билдер клавиатуры
    builder = InlineKeyboardBuilder()

    # Добавляем кнопки, группируя их по строкам
    builder.button(text=ButtonInl.tg_chn, url=ButtonInl.tg_chn_url)
    builder.button(text=ButtonInl.tg_chat, url=ButtonInl.tg_chat_url)

    builder.button(text=ButtonInl.web_text, url=ButtonInl.web_url)
    builder.button(text=ButtonInl.random_site, callback_data=ButtonInl.random_site_cbd)
    builder.button(text=ButtonInl.random_num_dice, callback_data=ButtonInl.random_num_dice_cbd)
    builder.button(text=ButtonInl.random_num_modal, callback_data=ButtonInl.random_num_modal_cdb)

    builder.adjust(2, 1)

    return builder.as_markup()


