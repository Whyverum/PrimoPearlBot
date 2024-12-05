# BotSettings/analitics/start_info_out.py
# Вывод данных бота в консоль для начальной проверки

from datetime import datetime
from time import sleep
from loguru import logger

from .. import ImportantPath
from ..library.bots import BotInfo
from ..library.decorator import TextDecorator

# Настройка экспорта
__all__ = ("bot_info_out",)
type_messages = "Start_INFO"


# Функция для получения информации о боте и выводе ее в консоль и файл
def bot_info_out():
    bot_time = f"Бот запущен в {datetime.now().strftime("%S:%M:%H %d-%m-%Y")}\n"
    bot_name = f"Основное имя: {BotInfo.first_name}\n"
    bot_postname = f" Доп. имя: {BotInfo.last_name}\n"
    bot_username = f" Юзернейм: @{BotInfo.username}\n"
    bot_id = f" ID: {BotInfo.id}\n"
    bot_language = f" Языковой код: {BotInfo.language_code}\n"
    bot_can_join_groups = f" Может ли вступать в группы: {BotInfo.can_join_groups}\n"
    bot_can_read_all_group_messages = f" Чтение всех сообщений: {BotInfo.can_read_all_group_messages}\n"
    bot_is_premium = f" Является премиум-ботом: {BotInfo.is_premium}\n"
    bot_added_to_attachment_menu = f" Добавлен в меню вложений: {BotInfo.added_to_attachment_menu}\n"
    bot_supports_inline_queries = f" Поддерживает инлайн-запросы: {BotInfo.supports_inline_queries}\n"
    bot_can_connect_to_business = f" Подключение к бизнес-аккаунтам: {BotInfo.can_connect_to_business}\n"
    bot_has_main_web_app = f" Основное веб-приложение: {BotInfo.has_main_web_app}\n"

    # Формируем полный текст с выводом информации о боте
    bot_all_info = (f"{bot_name} {bot_postname} {bot_username} {bot_id} {bot_language} "
                    f"{bot_can_join_groups} {bot_can_read_all_group_messages} {bot_is_premium} "
                    f"{bot_added_to_attachment_menu} {bot_supports_inline_queries} {bot_can_connect_to_business} "
                    f"{bot_has_main_web_app}")

    # Печатаем все данные в консоль с задержкой в 1 секунду
    sleep(1)
    print(TextDecorator.BLUE, bot_all_info, TextDecorator.RESET_DECORATOR)

    # Записываем информацию в файл
    try:
        with open(ImportantPath.log_info_path, 'w', encoding='utf-8') as log_file:
            log_file.write(f"{bot_time}{bot_all_info}")
        return bot_all_info

    # Проверка на ошибку и ее логирование
    except Exception as e:
        text_error = f"Ошибка при получении ID пользователя: {e}"
        logger.bind(custom_variable="INFO", user_var=type_messages).error(text_error)
        return text_error


