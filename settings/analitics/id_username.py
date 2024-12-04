# BotCode/settings/analitics/id_username.py    (в разработке + логирование ошибок сделать!!!!)

from ..library.bots import bot

# Работа с import *
__all__ = ("get_user_id_by_username", "get_user_id_username")
type_messages = "ID_USERNAME"


# Получение ID пользователя по юзернейму    (в разработке)
async def get_user_id_by_username(chat_id, username):
    try:
        user = await bot.get_chat_member_by_username(chat_id, username)
        if user:
            return user.user.id
        else:
            return None

    # Проверка на ошибку и ее логирование  (в разработке)
    except Exception as e:
        text_error = f"Ошибка при получении ID пользователя: {e}"
        print(text_error)
        return text_error


# Получение ID пользователя по юзернейму  (в разработке)
async def get_user_id_username(chat_id, username):
    try:
        user = await bot.get_chat_member_by_username(chat_id, username)
        if user and user.user:
            return user.user.id
        else:
            return None

    # Проверка на ошибку и ее логирование  (в разработке)
    except Exception as e:
        text_error = f"Ошибка при получении ID пользователя: {e}"
        print(text_error)
        return text_error
