# ban_cmd.py    (в разработке)

from aiogram import Router, types
from aiogram.filters import Command
from settings import *

# Создание роутера "ban_router"
router = Router(name="ban_router")
type_messages = "BAN"


@router.message(lambda message: message.from_user.id in ListId.ban_list_id)
async def banned_user(message: types.Message):
    name = await find_chat_id(message)
    text = f"Получено сообщение от забанненго пользователя из ({name}) : {message.text}"
    await logginger(message)
    logger.bind(custom_variable=type_messages, user_var=str(message.from_user.username)).info(text)
    await message.answer(f"Вы были забаннены!")
    return text


@router.message(Command("ban1", prefix=BotEdit.prefixs))
async def ban_user_by_username(message: types.Message):
    # Разбиваем сообщение на аргументы
    args = message.text.split()

    if len(args) < 2:
        await message.answer(f"Некорректный формат команды. Используйте: /ban1 @username")
        return

    # Получаем username из аргументов
    username = args[1].replace("@", "").strip()

    # Проверяем, чтобы username не был пустым
    if not username:
        await message.answer(f"Некорректный формат команды. Используйте: /ban1 @username")
        return

    # Получаем user_id по username
    user_id = 6813461867

    if user_id:
        # Баним пользователя по user_id
        await bot.ban_chat_member(chat_id=message.chat.id, user_id=user_id)
        await message.answer(f"Вы забанили пользователя с username @{username}.")
    else:
        await message.answer(f"Пользователь не найден.")
    return f"Бан - ура!"
