import asyncio, logging, datetime, os
from BotCode import config, func
from config import settings
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.client.bot import DefaultBotProperties
from aiogram.enums import ParseMode

#from routers import router as main_router

dp = Dispatcher()
#dp.include_routers(main_router)
times = datetime.datetime.now()


# Хэндлер на команду /start или /старт


# Хэндлер на админскую команду
@dp.message(F.from_user.id.in_(config.admin_id), F.text.lower() == "секрет")
async def secret_admin_message(message: types.Message):
    await message.reply("Привет админ!")
    await func.write_user_info_to_file(message.from_user)
    await func.write_message_to_file(message)


# Хэндлер на админскую команду
@dp.message(F.from_user.id.in_(config.admin_id), F.text.lower() == "финаки")
async def secret_admin_message(message: types.Message):
    await message.reply("Она кстати любит анал")
    await func.write_user_info_to_file(message.from_user)
    await func.write_message_to_file(message)


# Хэндлер на команду /info или /help


# Хэндлер на команду /id или /айди
@dp.message(Command("id", "айди", "myid", "мойайди", "myайди", "мойid", prefix=config.prefixs, ignore_case=True))
async def cmd_id(message: types.Message):
    user_id = message.from_user.id
    await message.answer(text=f"Ваш айди: <code>{user_id}</code>")
    await func.write_user_info_to_file(message.from_user)
    await func.write_message_to_file(message)



# Хэндлер на команду /chatid или /чатайди
@dp.message(Command("chatid", "чатайди", "chid", "чатid", "chatайди", "cid", prefix=config.prefixs, ignore_case=True))
async def cmd_chatid(message: types.Message):
    chat_id = message.chat.id
    await message.answer(text=f"Айди чата: <code>{chat_id}</code>")
    await func.write_user_info_to_file(message.from_user)
    await func.write_message_to_file(message)



# Хэндлер на команду /Привет или /hello
@dp.message(Command("Hello", "Hi", "Привет","Здравствуйте", "Прив", prefix=config.prefixs, ignore_case=True))
async def cmd_help(message: types.Message):
    await message.answer(text=f"Привет-привет!")
    await func.write_user_info_to_file(message.from_user)
    await func.write_message_to_file(message)



# Хэндлер на команду /download
# @dp.message(Command("download", "загрузка", "закачка", prefix=config.prefixs, ignore_case=True))
# async def cmd_download(message: types.Message):
#     url =
#     await func.dowland_youtube(url, config.youtube_path)
#     await func.write_user_info_to_file(message.from_user)
#     await func.write_message_to_file(message)
# # Пример использования
# url = "https://www.youtube.com/watch?v=ваш_идентификатор_видео"
# путь = "путь_к_папке_для_сохранения"


# Хэндлер на фотографию
@dp.message(F.photo)
async def handle_photo(message: types.Message, bot: Bot):
    result = await func.download_image(message.photo, bot)

    await func.write_user_info_to_file(message.from_user)
    await func.write_message_to_file(message)


@dp.message(F.document | F.video | F.animation | F.voice | F.video_note)
async def handle_media(message: types.Message, bot: Bot):
    # Определяем базовый путь для сохранения медиа

    # Обработка видео и анимации
    if message.content_type in (types.ContentType.VIDEO, types.ContentType.ANIMATION):
        await func.write_user_info_to_file(message.from_user)
        await func.write_message_to_file(message)

        media = message.video if message.content_type == types.ContentType.VIDEO else message.animation
        file_name = media.file_name if media.file_name else f"{'video' if message.content_type == types.ContentType.VIDEO else 'gif'}_{media.file_id}"
        file_extension = media.mime_type.split('/')[-1]
        file_name_with_extension = f"{file_name}.{file_extension}"

        save_path = os.path.join(config.base_path, 'Video' if message.content_type == types.ContentType.VIDEO else 'GIF')
        os.makedirs(save_path, exist_ok=True)  # Создаём директорию, если её нет

        file = await bot.get_file(media.file_id)
        await bot.download_file(file.file_path, os.path.join(save_path, file_name_with_extension))

    # Обработка документов
    elif message.content_type == types.ContentType.DOCUMENT:
        await func.write_user_info_to_file(message.from_user)
        await func.write_message_to_file(message)

        file_id = message.document.file_id
        file = await bot.get_file(file_id)
        file_name = message.document.file_name
        file_path = file.file_path

        save_path = os.path.join(config.base_path, 'Document')
        os.makedirs(save_path, exist_ok=True)  # Создаём директорию, если её нет

        await bot.download_file(file_path, os.path.join(save_path, file_name))

    # Обработка голосовых сообщений
    elif message.content_type == types.ContentType.VOICE:
        await func.write_user_info_to_file(message.from_user)
        await func.write_message_to_file(message)

        media = message.voice
        file_name = f"voice_{media.file_id}.ogg"  # Уникальное имя для голосовых сообщений

        save_path = os.path.join(config.base_path, 'Voice')
        os.makedirs(save_path, exist_ok=True)  # Создаём директорию, если её нет

        file = await bot.get_file(media.file_id)
        await bot.download_file(file.file_path, os.path.join(save_path, file_name))

    # Обработка видео сообщений (video notes)
    elif message.content_type == types.ContentType.VIDEO_NOTE:
        await func.write_user_info_to_file(message.from_user)
        await func.write_message_to_file(message)

        media = message.video_note
        file_name = f"video_note_{media.file_id}.mp4"

        save_path = os.path.join(config.base_path, 'VideoNote')
        os.makedirs(save_path, exist_ok=True)  # Создаём директорию, если её нет

        file = await bot.get_file(media.file_id)

        await bot.download_file(file.file_path, os.path.join(save_path, file_name))


# Хэндлер на все входящие сообщения
@dp.message()
async def handle_all_messages(message: types.Message):
    await func.write_user_info_to_file(message.from_user)
    await func.write_message_to_file(message)
    if message.text and message.text.lower() == "кошмар":
        await message.answer("Кошмар, тот еще!")



async def main():
    bot = Bot(token=settings.bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    bot_info_str, bot_first_name, bot_username = await func.get_bot_info(bot)
    logging.basicConfig(level=logging.DEBUG)
    print(bot_info_str)

    await func.write_bot_start_info(config.log_file_path, bot_first_name, bot_username)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())