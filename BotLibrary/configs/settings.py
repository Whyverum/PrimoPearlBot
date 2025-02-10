# BotLibrary/configs/settings.py
# Список практически всех переменных проекта

from os import getenv
from dotenv import load_dotenv


# Базовая кодировка файлов
default_encod = "utf-8"

# Создание класса с временными параметрами
class TimeVariable:
    format = "%Y-%m-%d %H:%M:%S"
    another_format = "%S:%M:%H %d-%m-%Y"
    choice_main_utc = "Asia/Novosibirsk"
    choice_utc_msk = "Europe/Moscow"
    choice_utc_krsk = "Asia/Krasnoyarsk"  # Новый выбор для Красноярска


# Класс с параметрами бота
class BotEdit:
    name = "Первородная Жемчужина"  # Описание имени бота
    description = ("Привет, мое имя - Эми! Я буду рада помочь вам "
                   "посетить другие миры! Вместе!")  # Описание бота
    short_description = "Привет, это описание! Как дела?"  # Описание виджета бота


# Важные параметры бота
class BotVariables:
    language = "Python3-Aiogram"
    prefixs = ('$', '!', '.', '%', '&', ':', '|', '+', '-', '/', '~', '?')


# Загружаем переменные из файла ProjectsFile/.env
load_dotenv("ProjectsFile/.env")

bot_token = getenv("BOT_TOKEN")
bot1_token = getenv("BOT1_TOKEN")
bot2_token = getenv("BOT2_TOKEN")

api_key = getenv("API_KEY")
web_api_key = getenv("WEB_API_KEY")

tg_api_uid = getenv("TG_API_UID")
tg_api_hash = getenv("TG_API_HASH")

admin_id = getenv("ADMIN_ID")
important_id = getenv("IMPORTANT_ID")
important_group_id = getenv("IMPORTANT_GROUP_ID")
important_channel_id = getenv("IMPORTANT_CHANNEL_ID")

secret = getenv("SECRET")
