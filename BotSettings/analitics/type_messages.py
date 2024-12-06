# BotSettings/analitics/type_messages.py
# Определение типа сообщения

from BotSettings.library.config import BotEdit

# Настройка экспорта модулей
__all__ = ("types_message",)
type_messages = "Type_message"


# Проверка на тип сообщения
def types_message(message):
    if message.text:
        first_char = message.text.strip()[0]  # Извлекаем первый символ текста (убираем лишние пробелы)
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
        file_type = "Видеосообщение"
    elif message.video_note:
        file_type = "Голосовое сообщение"
    elif message.video:
        file_type = "Видео"
    elif message.audio:
        file_type = "Аудио"
    elif message.document:
        file_type = "Документ"
    elif message.contact:
        file_type = "Контакт"
    elif message.location:
        file_type = "Локация"
    elif message.venue:
        file_type = "Venue"
    elif message.dice:
        file_type = "Бросок"
    elif message.story:
        file_type = "История"
    elif message.game:
        file_type = "Игра"
    elif message.new_chat_members:
        file_type = "Участник присоединился к нам!"
    elif message.left_chat_member:
        file_type = "Участник покинул чат..."
    elif message.boost_added:
        file_type = "Бууууст!"
    elif message.poll:
        file_type = "Опрос"
    else:
        file_type = "ОШИБКА! ОШИБКА!! ОШИБКА!!! НЕИЗВЕСТНЫЙ ТИП!!!!"
    return file_type
