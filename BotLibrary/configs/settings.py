# BotLibrary/configs/settings.py
# Список практически всех переменных проекта

from os import getenv
from dotenv import load_dotenv

# Настройка экспорта модулей
__all__ = ("BotEdit", "BotVariables", "bot_token", "api_key",
           "web_api_key", "important_id", "secret")


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


# Загружаем переменные из файла .env
load_dotenv(".env")
bot_token = getenv("main_bot_token")
api_key = getenv("APIKey")
web_api_key = getenv("WebAPIKey")
important_id = getenv("important_id")
secret = getenv("secret")
