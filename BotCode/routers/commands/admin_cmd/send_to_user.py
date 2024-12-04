# send_massage_handlers.py  (в разработке)

from aiogram import Router, types, F
from aiogram.filters import Command
from settings import *

router = Router(name="send_router")
type_messages = "Send"


# Обработчик команды /send для отправки сообщения определенному пользователю    (в разработке)
@router.message(F.from_user.id.in_(ListId.important_ids),
                Command("send", "отправить", "отправ", "s", "ыутв", "jnghfdbnm", "jnghfd",
                        prefix=BotEdit.prefixs, ignore_case=True))
async def send_message(message: types.Message):
    if message.chat.id in ListId.adm_list_id:
        # Разбиваем сообщение на аргументы
        args = message.text.split()

        # Проверка на правильность команды /send
        if len(args) < 3:
            text = "Некорректный формат команды. Используйте: /send <user_id> <текст>"
            await message.answer(text)
            return text

        # Получаем user_id и текст сообщения
        user_id = int(args[1])
        text = ' '.join(args[2:])

        # Отправляем сообщение пользователю
        await bot.send_message(chat_id=user_id, text=text)

        # Логирование
        if user_id in ListId.important_ids:
            user_id = ListId.important_ids[user_id]
        logger.bind(custom_variable=type_messages, user_var=str(message.from_user.username)).info(
            f"Сообщение от @{BotInfo.username} для @{user_id}: {text}")

        # Логирование и отчет об отправке
        await logginger(message)
        await message.answer(f"Сообщение успешно отправлено пользователю с ID {user_id}")
        return

    # except exceptions.BotBlocked:
    #     await message.answer("Пользователь заблокировал бота")
    #     except aiogram.utils.exceptions.ChatNotFound:
    #     await message.answer("Чат с пользователем не найден")
    # except exceptions.RetryAfter as e:
    #     await asyncio.sleep(e.timeout)
    #     return await send_message(message)
    # except exceptions.UserDeactivated:
    #     await message.answer("Пользователь деактивирован")
    # except exceptions.TelegramAPIError:
    #     await message.answer("Произошла ошибка при отправке сообщения")
    # except:
    #     return
