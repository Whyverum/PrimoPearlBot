# exit_cmd.py   (в разработке)

from aiogram import Router, types
from aiogram.filters import Command
from settings import *

router = Router(name="exit_router")
type_messages = "Exit"


# Обработчик команды /выход  (в разработке)
@router.message(Command("выход", "ds[j;", "exit", "учше", prefix=BotEdit.prefixs, ignore_case=True))
async def exit_cmd(message: types.Message):
    try:
        text = f"Пользователь успешно вышел из чата!"
        logger.bind(custom_variable=type_messages, user_var=str(message.from_user.username)).info(text)
        await bot.ban_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
        await message.answer(f"Вы забанили этого пользователя.")
        return text

    # Проверка на ошибку и ее логирование   (В разработке)
    except Exception as e:
        text_error = f"Ошибка при использовании команды /{type_messages.lower()}: {str(e)}\n"
        await setup_error_logger()
        logger.bind(custom_variable=type_messages, user_var=f"@{message.from_user.username}").error(text_error)
        await setup_logger()
        return text_error
