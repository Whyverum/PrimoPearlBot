# BotSettings/library/bots.py
# Создание и настройка бота в одном файле

from aiogram import Bot, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from ..configs.bot_secrets import bot_token

# Настройка экспорта модулей
__all__ = ("bot_token", "bot", "scheduler", "F_Media", "BotInfo", "bot_get_info")


# Объявление экземпляров и переменных
bot_token = bot_token   # Объявление ключа бота
bot = Bot(token=bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))     # Объявление бота
scheduler = AsyncIOScheduler(timezone='Asia/Novosibirsk')   # Создание планировщика
F_Media = F.photo | F.document | F.video | F.animation | F.voice | F.video_note  # Фильтр-медиа


# Класс для хранения данных о боте
class BotInfo:
    # Статические переменные для хранения данных
    id = None
    first_name = None
    last_name = None
    username = None
    can_join_groups = None
    can_read_all_group_messages = None
    language_code = "Python-Aiogram"
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
        'language_code': "Python-Aiogram",
        'is_premium': bot_info_data.is_premium,
        'added_to_attachment_menu': bot_info_data.added_to_attachment_menu,
        'supports_inline_queries': bot_info_data.supports_inline_queries,
        'can_connect_to_business': bot_info_data.can_connect_to_business,
        'has_main_web_app': bot_info_data.has_main_web_app,
    }
