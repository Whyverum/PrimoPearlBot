# BotLibrary/analitics/start_info_out.py
# Вывод данных бота в консоль для начальной проверки
# Логирование стартов бота в bot_start.log

from datetime import datetime
from colorama import Fore
from loguru import logger
from time import sleep

from ..configs import ProjectPath, default_encod
from BotLibrary.timers.time import TimeVariable
from ..library.bots import BotInfo

# Настройка экспорта модулей и логирования
__all__ = ("bot_info_out",)
log_type = "Start_INFO"


# Функция для получения информации о боте и выводе ее в консоль и файл
def bot_info_out():
    bot_time = f"Бот @{BotInfo.username} запущен в {datetime.now().strftime(TimeVariable.format)}\n"
    bot_name = f"Основное имя: {BotInfo.first_name}\n"
    bot_postname = f" Доп. имя: {BotInfo.last_name}\n"
    bot_username = f" Юзернейм: @{BotInfo.username}\n"
    bot_id = f" ID: {BotInfo.id}\n"
    bot_language = f" Языковой код: {BotInfo.language_code}\n"
    bot_can_join_groups = f" Может ли вступать в группы: {BotInfo.can_join_groups}\n"
    bot_can_read_all_group_messages = f" Чтение всех сообщений: {BotInfo.can_read_all_group_messages}\n"  # Теперь атрибут существует
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
    print(Fore.CYAN + bot_all_info)

    # Записываем информацию в файл
    try:
        with open(ProjectPath.log_info, 'w', encoding=default_encod) as log_file:
            log_file.write(f"{bot_time}{bot_all_info}")

        # Создание файла bot_start.log
        with open(ProjectPath.log_start, 'a', encoding=default_encod) as log_start_file:
            log_start_file.write(f"{bot_time}\n")

        return bot_all_info

    # Проверка на ошибку и ее логирование
    except Exception as e:
        text_error = f"Ошибка при получении ID пользователя: {e}"
        logger.bind(log_type="INFO", user=log_type).error(text_error)
