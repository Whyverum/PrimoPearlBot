# BotLibrary/analitics/log_type.py
# Определение типа сообщения

from aiogram.types import ContentType
from configs import *
from .find_ids import find_imp_id

# Настройка экспорта модулей и логирования
__all__ = ("types_message", "types_chat",)
log_type = "Type_message"


# Проверка на тип чата
def types_chat(message):
    user_id = find_imp_id(message.from_user.id)
    chat_id = find_imp_id(message.chat.id)
    if message.chat.type == "private":
        file_path = f"{ProjectPath.private_message}/{user_id}.txt"
    else:
        file_path = f"{ProjectPath.group_message}/{chat_id}.txt"
    return file_path


def types_message(message):
    # Словарь для соответствия типов сообщений
    content_types = {
        ContentType.TEXT: "Текст",
        ContentType.PHOTO: "Фото",
        ContentType.STICKER: "Стикер",
        ContentType.ANIMATION: "Гиф",
        ContentType.VOICE: "Голосовое сообщение",
        ContentType.VIDEO_NOTE: "Видеосообщение",
        ContentType.VIDEO: "Видео",
        ContentType.AUDIO: "Аудио",
        ContentType.DOCUMENT: "Документ",
        ContentType.CONTACT: "Контакт",
        ContentType.LOCATION: "Локация",
        ContentType.VENUE: "Место",
        ContentType.DICE: "Бросок кубика",
        ContentType.STORY: "История",
        ContentType.GAME: "Игра",
        ContentType.POLL: "Опрос",
        ContentType.FORUM_TOPIC_CREATED: "Создание темы на форуме",
        ContentType.FORUM_TOPIC_EDITED: "Редактирование темы форума",
        ContentType.FORUM_TOPIC_CLOSED: "Закрытие темы форума",
        ContentType.FORUM_TOPIC_REOPENED: "Открытие темы форума",
        ContentType.GENERAL_FORUM_TOPIC_HIDDEN: "Скрытие общей темы форума",
        ContentType.GENERAL_FORUM_TOPIC_UNHIDDEN: "Раскрытие общей темы форума",
        ContentType.GIVEAWAY_CREATED: "Создание розыгрыша",
        ContentType.GIVEAWAY: "Розыгрыш",
        ContentType.GIVEAWAY_WINNERS: "Победители розыгрыша",
        ContentType.GIVEAWAY_COMPLETED: "Розыгрыш завершен",
        ContentType.VIDEO_CHAT_SCHEDULED: "Запланированный видеочат",
        ContentType.VIDEO_CHAT_STARTED: "Видеочат начат",
        ContentType.VIDEO_CHAT_ENDED: "Видеочат завершен",
        ContentType.VIDEO_CHAT_PARTICIPANTS_INVITED: "Участники приглашены в видеочат",
        ContentType.PINNED_MESSAGE: "Закрепленное сообщение",
        ContentType.INVOICE: "Счет",
        ContentType.SUCCESSFUL_PAYMENT: "Успешный платеж",
        ContentType.REFUNDED_PAYMENT: "Возврат платежа",
        ContentType.USERS_SHARED: "Пользователи поделились",
        ContentType.CHAT_SHARED: "Чат был передан",
        ContentType.CONNECTED_WEBSITE: "Подключенный веб-сайт",
        ContentType.WRITE_ACCESS_ALLOWED: "Разрешение на запись",
        ContentType.PASSPORT_DATA: "Данные паспорта",
        ContentType.PROXIMITY_ALERT_TRIGGERED: "Срабатывание предупреждения о близости",
        ContentType.BOOST_ADDED: "Буст чата",
        ContentType.CHAT_BACKGROUND_SET: "Установлен фон чата"
    }

    # Проверяем тип сообщения и возвращаем описание
    if message.pinned_message:  # Закрепленное сообщение
        return content_types.get(ContentType.PINNED_MESSAGE, "Закрепленное сообщение")

    # Проверка для обычных сообщений
    for content_type, description in content_types.items():
        if getattr(message, content_type.value, None):
            return description

    # Если сообщение не соответствует ни одному из типов
    return "Неизвестный тип сообщения"
