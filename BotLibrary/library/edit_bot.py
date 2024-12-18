# BotLibrary/system/edit_bot.py
# Библиотека установки настроек бота через проект и конфиги

from aiogram.types import ChatAdministratorRights
from loguru import logger

from config import BotEdit
from BotLibrary.library.bots import bot

# Настройка экспорта модулей и логирования
__all__ = ("set_all", "set_adm_rights", "set_bot_name",
           "set_bot_description", "set_bot_short_description")
log_type = "Edit"


# Функция для выполнения всех настроек, если они не совпадают
async def set_all():
    await set_adm_rights()
    await set_bot_name()
    await set_bot_description()
    await set_bot_short_description()
    return f"Автономная настройка бота - завершена!"


# Функция установки имени бота с проверкой на ограничения
async def set_bot_name():
    # Получаем текущее имя бота
    current_name = (await bot.get_me()).first_name

    # Проверка длины имени
    if len(BotEdit.name) < 1 or len(BotEdit.name) > 32:
        # Логируем ошибку, если имя не соответствует ограничению
        (logger.bind(log_type=log_type, user="NAME_BOT")
         .error("Имя бота должно быть от 1 до 32 символов."))

        # Возвращаем сообщение о неверном имени
        return "Ошибка: Имя бота должно быть от 1 до 32 символов."

    # Проверяем, совпадает ли текущее имя с тем, которое мы хотим установить
    if current_name != BotEdit.name:
        await bot.set_my_name(BotEdit.name)
        return f"Имя бота изменено на {BotEdit.name}!"
    else:
        return f"Имя бота уже установлено как {current_name}. Изменений не требуется."


# Функция установки прав администратора
async def set_adm_rights():
    # Применить права администратора для бота
    rights = ChatAdministratorRights(
        is_anonymous=False,
        can_manage_chat=True,
        can_delete_messages=True,
        can_manage_video_chats=True,
        can_restrict_members=True,
        can_promote_members=True,
        can_change_info=True,
        can_invite_users=True,
        can_post_stories=True,
        can_edit_stories=True,
        can_delete_stories=True,
        can_post_messages=True,
        can_edit_messages=True,
        can_pin_messages=True,
        can_manage_topics=True,
    )

    # Применяем права только в случае изменения
    current_rights = await bot.get_my_default_administrator_rights()
    if current_rights != rights:
        await bot.set_my_default_administrator_rights(rights)
        return f"Админ права бота изменены!"
    else:
        return f"Админ права уже установлены и не требуют изменений."


# Функция установки описания бота с проверкой на ограничения
async def set_bot_description():
    # Получаем текущее описание бота
    current_description = await bot.get_my_description()

    # Проверка длины описания
    if len(BotEdit.description) > 255:
        (logger.bind(log_type=log_type, user="DISCRIPT")
         .error("Короткое описание бота не может превышать 255 символов."))

    # Проверяем, совпадает ли текущее описание с тем, которое мы хотим установить
    if current_description != BotEdit.description:
        await bot.set_my_description(description=BotEdit.description)
        return f"Описание бота изменено!"
    else:
        return f"Описание бота уже установлено и не требует изменений."


# Функция установки короткого описания бота с проверкой на ограничения
async def set_bot_short_description():
    # Получаем текущее короткое описание бота
    current_short_description = await bot.get_my_short_description()

    # Проверка длины короткого описания
    if len(BotEdit.short_description) > 512:
        (logger.bind(log_type=log_type, user="SHORT_DISCRIPT")
         .error("Описание бота не может превышать 512 символов."))

    # Проверяем, совпадает ли текущее короткое описание с тем, которое мы хотим установить
    if current_short_description != BotEdit.short_description:
        await bot.set_my_short_description(short_description=BotEdit.short_description)
        return f"Короткое описание бота изменено!"
    else:
        return f"Короткое описание бота уже установлено и не требует изменений."
