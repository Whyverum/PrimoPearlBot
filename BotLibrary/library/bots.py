# BotLibrary/library/bots.py
# Создание и настройка бота в одном файле

import pytz
from tzlocal import get_localzone
from datetime import datetime
from aiogram import Dispatcher, Bot, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from config import bot_token, BotVariables

# Настройка экспорта модулей и логирования
__all__ = ("bot_token", "dp", "bot", "scheduler", "F_Media", "BotInfo", "bot_get_info")
log_type = "Bot"


# Получение времени по UTC
utc_now = datetime.now(pytz.utc)

# Получение локального времени хоста (с использованием локального часового пояса)
local_tz = get_localzone()  # Автоматически определяет локальный часовой пояс
local_now = utc_now.astimezone(local_tz)

# Получение московского времени
moscow_tz = pytz.timezone("Europe/Moscow")
moscow_now = utc_now.astimezone(moscow_tz)

# Форматирование времени UTC
utc_time = utc_now.strftime("%Y-%m-%d %H:%M:%S") + " (UTC)"

# Форматирование времени хоста со сдвигом
utc_offset_host = local_now.utcoffset().total_seconds() / 3600  # Смещение в часах
host_time = local_now.strftime("%Y-%m-%d %H:%M:%S") + f" (UTC{int(utc_offset_host):+})"

# Форматирование московского времени со сдвигом
utc_offset_moscow = moscow_now.utcoffset().total_seconds() / 3600  # Смещение в часах
moscow_time = moscow_now.strftime("%Y-%m-%d %H:%M:%S") + f" (UTC{int(utc_offset_moscow):+})"


# Создание экземпляра диспатчера и его параметров
dp = Dispatcher()
dp["started_at"] = host_time
dp["started_at_msk"] = moscow_time
dp["is_active"] = True  # Флаг активности бота
dp["logs"] = []
dp["users"] = {}
dp["sessions"] = {}
dp["task_queue"] = []
dp["config"] = {"max_connections": 100, "retry_interval": 5, "time_format": BotVariables.time_format}
dp["metrics"] = {"messages_received": 0, "messages_sent": 0, "errors": 0}
dp["modules"] = {}
dp["state"] = {}
dp["scheduler"] = []
dp["handlers"] = {"on_message": [], "on_error": []}
dp["storage"] = {}
dp["database"] = None


# Объявление экземпляров и переменных
bot = Bot(token=bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))     # Объявление бота
scheduler = AsyncIOScheduler(timezone=BotVariables.time_zone)   # Создание планировщика
F_Media = F.photo | F.files | F.video | F.animation | F.voice | F.video_note  # Фильтр-медиа


# Класс для хранения данных о боте (некоторые переменные даны как шаблон)
class BotInfo:
    # Статические переменные для хранения данных
    id = 10000000
    first_name = "TESTBOT"
    last_name = ""
    username = "testbot"
    can_join_groups = None
    can_read_all_group_messages = None
    language_code = BotVariables.language
    is_premium = None
    added_to_attachment_menu = None
    supports_inline_queries = None
    can_connect_to_business = None
    has_main_web_app = None

    # Метод для обновления данных
    @classmethod
    def update(cls, bot_info):
        cls.id = bot_info.id
        cls.first_name = bot_info.first_name
        cls.last_name = bot_info.last_name
        cls.username = bot_info.username
        cls.can_join_groups = bot_info.can_join_groups
        cls.can_read_all_group_messages = bot_info.can_read_all_group_messages
        cls.is_premium = bot_info.is_premium
        cls.added_to_attachment_menu = bot_info.added_to_attachment_menu
        cls.supports_inline_queries = bot_info.supports_inline_queries
        cls.can_connect_to_business = bot_info.can_connect_to_business
        cls.has_main_web_app = bot_info.has_main_web_app


# Функция получения данных о боте
async def bot_get_info():
    # Получение информации о боте
    bot_info_data = await bot.get_me()

    # Обновляем данные о боте в BotInfo
    BotInfo.update(bot_info_data)

    # Возвращаем обновленные данные
    return {
        'bot_info': bot_info_data,
        'id': bot_info_data.id,
        'first_name': bot_info_data.first_name,
        'last_name': bot_info_data.last_name,
        'username': bot_info_data.username,
        'can_join_groups': bot_info_data.can_join_groups,
        'can_read_all_group_messages': bot_info_data.can_read_all_group_messages,
        'language_code': BotVariables.language,
        'is_premium': bot_info_data.is_premium,
        'added_to_attachment_menu': bot_info_data.added_to_attachment_menu,
        'supports_inline_queries': bot_info_data.supports_inline_queries,
        'can_connect_to_business': bot_info_data.can_connect_to_business,
        'has_main_web_app': bot_info_data.has_main_web_app,
    }
