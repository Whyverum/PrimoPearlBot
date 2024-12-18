# BotLibrary/analitics/log_type.py
# Определение типа сообщения

from .find_ids import find_chat_id
from config import BotEdit, ImportantPath

# Настройка экспорта модулей и логирования
__all__ = ("types_message", "types_chat",)
log_type = "Type_message"


# Проверка на тип чата
def types_chat(message):
    chat_id = find_chat_id(message)
    if message.chat.type == "private":
        file_path = f"{ImportantPath.private_message}/{chat_id}.txt"
    else:
        file_path = f"{ImportantPath.group_message}/{chat_id}.txt"
    return file_path


# Проверка на тип сообщения
def types_message(message):
    if message.pinned_message:  # Закрепленное сообщение
        file_type = "Закрепленное сообщение"
    elif message.text:
        first_char = message.text.strip()[0] if message.text.strip() else ""  # Извлекаем первый символ текста
        if first_char in BotEdit.prefixs:
            file_type = "Команда"
        else:
            file_type = "Текст"
    elif message.photo:
        file_type = "Фото"
    elif message.sticker:
        file_type = "Стикер"
    elif message.animation:
        file_type = "Гиф"
    elif message.voice:
        file_type = "Голосовое сообщение"
    elif message.video_note:
        file_type = "Видеосообщение"
    elif message.video:
        file_type = "Видео"
    elif message.audio:
        file_type = "Аудио"
    elif message.files:
        file_type = "Документ"
    elif message.contact:
        file_type = "Контакт"
    elif message.location:
        file_type = "Локация"
    elif message.venue:
        file_type = "Место"
    elif message.dice:
        file_type = "Бросок кубика"
    elif message.story:
        file_type = "История"
    elif message.game:
        file_type = "Игра"
    elif message.new_chat_members:
        file_type = (f"Участник(и) присоединился(ись): "
                     f"{', '.join([member.username for member in message.new_chat_members if member.username])}")
    elif message.left_chat_member:
        file_type = f"Участник покинул чат: {message.left_chat_member.username or 'Неизвестный'}"
    elif getattr(message, 'boost_added', False):  # Проверяем наличие атрибута boost_added
        file_type = "Буст чата!"
    elif message.poll:
        file_type = "Опрос"
    elif message.forward_from or message.forward_from_chat:
        file_type = "Пересланное сообщение"
    else:
        file_type = "Неизвестный тип сообщения"
    return file_type
