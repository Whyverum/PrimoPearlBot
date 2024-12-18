# BotLibrary/analitics/find_ids.py
# Проверка пользователя на нахождение в списках бота

from aiogram import types
from config import ListId

# Настройка экспорта модулей и логирования
__all__ = ("find_people_id", "find_chat_id", "find_adm_id", "find_ban_id")
log_type = "ID"


# Функция поиска человека в списке администраторов
def find_adm_id(message):
    if message.from_user.id in ListId.adm_list_id:
        return True
    else:
        return f"Пользователь не является администратором!"


# Функция поиска человека в списке администраторов
def find_ban_id(message):
    if message.from_user.id in ListId.ban_list_id:
        return True
    else:
        return f"Пользователь не забанен!"


# Функция поиска человека в списке "важных" пользователей
def find_people_id(user_id):
    # Проверка на наличие пользователя в списке "важных" пользователей
    if user_id in ListId.important_ids:
        user_id = ListId.important_ids[user_id]
    return user_id


# Проверка на наличие чата в списке "важных" чатов
def find_chat_id(message: types.Message):
    chat_id = message.chat.id
    # Проверка на наличие чата в списке "важных" чатов
    if chat_id in ListId.important_ids:
        chat_id = ListId.important_ids[chat_id]
    return chat_id
