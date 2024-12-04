# BotCode/settings/analitics/find_adm_list_id.py

from aiogram import types
from ..configs.config import ListId

# То что будет импортироваться при from find_adm_list import *
__all__ = ("find_people_id", "find_chat_id")
type_messages = "ID"


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
