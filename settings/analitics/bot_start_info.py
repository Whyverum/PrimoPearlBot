# BotCode/settings/analitics/bot_start_info.py

from ..library.bots import BotInfo
from ..library.decorator import TextDecorator

# То что будет импортироваться при from bot_start_info import *
__all__ = ("bot_info_out",)
type_messages = "Start_INFO"


# Функция для получения информации о боте и выводе ее в консоль
async def bot_info_out():
    bot_name = f"Основное имя: {BotInfo.first_name}\n"
    bot_postname = f"Доп. имя: {BotInfo.last_name}\n"
    bot_username = f"Юзернейм: @{BotInfo.username}\n"
    bot_id = f"ID: {BotInfo.id}\n"
    bot_language = f"Языковой код: {BotInfo.language_code}\n"
    bot_can_join_groups = f"Может ли вступать в группы?: {BotInfo.can_join_groups}\n"
    bot_can_read_all_group_messages = f"Чтение всех сообщений: {BotInfo.can_read_all_group_messages}\n"
    bot_is_premium = f"Является премиум-ботом?: {BotInfo.is_premium}\n"
    bot_added_to_attachment_menu = f"Добавлен в меню вложений?: {BotInfo.added_to_attachment_menu}\n"
    bot_supports_inline_queries = f"Поддерживает инлайн-запросы?: {BotInfo.supports_inline_queries}\n"
    bot_can_connect_to_business = f"Может ли подключаться к бизнес-аккаунтам?: {BotInfo.can_connect_to_business}\n"
    bot_has_main_web_app = f"Есть ли основное веб-приложение?: {BotInfo.has_main_web_app}\n"

    # Формируем полный текст с выводом информации о боте
    bot_all_info = (f"{TextDecorator.BLUE} {bot_name} {bot_postname} {bot_username} {bot_id} "
                    f"{bot_language} {bot_can_join_groups} {bot_can_read_all_group_messages} {bot_is_premium} "
                    f"{bot_added_to_attachment_menu} {bot_supports_inline_queries} {bot_can_connect_to_business} "
                    f"{bot_has_main_web_app} {TextDecorator.RESET_DECORATOR}")

    # Печатаем все данные в консоль
    print(bot_all_info)
    return bot_all_info
