# admin_handlers.py

from aiogram.filters import Command
from loguru import logger
from aiogram import Router, F, types

from BotCode import config
from BotCode.routers.administration.analitics_handlers import write_message_to_file

router = Router(name=__name__)


# Получение ID пользователя по юзернейму
async def get_user_id_by_username(chat_id, username):
    try:
        user = await config.bots.get_chat_member_by_username(chat_id, username)
        if user:
            return user.user.id
        else:
            return None
    except Exception as e:
        print(f"Ошибка при получении ID пользователя: {e}")
        return None


# Обработчик команды /ban1 @username
@router.message(Command("ban1", prefix=config.prefix))
async def ban_user_by_username(message: types.Message):
    # Разбиваем сообщение на аргументы
    args = message.text.split()

    if len(args) < 2:
        await message.answer("Некорректный формат команды. Используйте: /ban1 @username")
        return

    # Получаем username из аргументов
    username = args[1].replace("@", "")

    # Получаем user_id по username
    user_id = await get_user_id_by_username(message.chat.id, username)
    print(user_id)

    if user_id:
        # Баним пользователя по user_id
        await config.bots.ban_chat_member(chat_id=message.chat.id, user_id=user_id)
        await message.answer(f"Вы забанили пользователя с username {username}.")
    else:
        await message.answer("Пользователь не найден.")



# Получение ID пользователя по юзернейму
async def get_user_id_by_username(chat_id, username):
    try:
        user = await config.bots.get_chat_member_by_username(chat_id, username)
        if user:
            print(user.user.id)
            return user.user.id
        else:
            return None
    except Exception as e:
        print(f"Ошибка при получении ID пользователя: {e}")
        return None






# Обработчик команды /выход
@router.message(Command("выход", prefix=config.prefix))
async def ban_user(message: types.Message):
    await config.bots.ban_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
    await message.answer("Вы забанили этого пользователя.")


# Хэндлер на текстовое сообщение "secret"
@router.message(F.from_user.id.in_(config.important_ids), F.text.lower() == "secret")
async def secret_admin_message(message: types.Message):
    await message.reply("Привет, админ!")
    await write_message_to_file(message)
    logger.bind(custom_variable="Admin", user_var=str(message.from_user.username)).info("Сообщение secret получено!")

# Хэндлер на цифирный код
# @router.message(
#     F.from_user.id.in_(config.admin_ids),
#     F.text.regexp(r"(\d+)", mode=RegexpMode.MATCH).as_("code"),
# )
# async def handle_code(message: types.Message, code: Match[str]):
# await message.reply(f"Your code: {code.group()}")
# await write_user_info_to_file(message.from_user)
# await write_message_to_file(message)
