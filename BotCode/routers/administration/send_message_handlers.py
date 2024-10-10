# send_massage_handlers.py
from loguru import logger
from aiogram import Router, F
from BotCode import config
from BotCode.routers.administration.analitics_handlers import loginger
from aiogram import types
from aiogram.filters import Command

router = Router(name=__name__)


# Обработчик команды /send
@router.message(F.from_user.id.in_(config.important_ids), Command("send", "отправить", "отправ", "s",
                                                                  prefix=config.prefix, ignore_case=True))
async def send_message(message: types.Message):
    if message.chat.id in config.important_adm_id:
        # Разбиваем сообщение на аргументы
        args = message.text.split()

        if len(args) < 3:
            await message.answer("Некорректный формат команды. Используйте: /send <user_id> <текст>")
            return

        # Получаем user_id и текст сообщения
        user_id = int(args[1])
        text = ' '.join(args[2:])

        # Отправляем сообщение пользователю
        await config.bots.send_message(chat_id=user_id, text=text)

        # Логирование
        if user_id in config.important_ids:
            user_id = config.important_ids[user_id]
        logger.bind(custom_variable="Send", user_var=str(message.from_user.username)).info(
            f"Сообщение от @{config.bot_username} для @{user_id}: {text}")

        await loginger(message)
        await message.answer(f"Сообщение успешно отправлено пользователю с ID {user_id}")

    # except exceptions.BotBlocked:
    #     await message.answer("Пользователь заблокировал бота")
    #     except aiogram.utils.exceptions.ChatNotFound:
    #     await message.answer("Чат с пользователем не найден")
    # except exceptions.RetryAfter as e:
    #     awaitt asyncio.sleep(e.timeout)
    #     return await send_message(message)
    # except exceptions.UserDeactivated:
    #     await message.answer("Пользователь деактивирован")
    # except exceptions.TelegramAPIError:
    #     await message.answer("Произошла ошибка при отправке сообщения")
    # except:
    #     return
