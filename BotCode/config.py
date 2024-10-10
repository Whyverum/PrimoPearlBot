# config.py

from aiogram import Bot, F
from aiogram.client.bot import DefaultBotProperties
from aiogram.enums import ParseMode
from BotInfo import bot_secrets

bot_token = bot_secrets.PrimoTester_bot_token  # API ключ бота
parse_mode = DefaultBotProperties(parse_mode=ParseMode.HTML)  # Стандартный парс мод
bots = Bot(token=bot_token, default=parse_mode)  # Объявление бота
bot_language = "Python-Aiogram"


async def get_info(bot):
    global bot_info, bot_id, bot_first_name, bot_last_name, bot_username, \
        bot_language_code, bot_can_join_groups, bot_can_read_all_group_messages
    bot_info = await bot.get_me()
    bot_id = bot_info.id
    bot_first_name = bot_info.first_name
    bot_last_name = bot_info.last_name
    bot_username = bot_info.username
    bot_can_join_groups = bot_info.can_join_groups
    bot_can_read_all_group_messages = bot_info.can_read_all_group_messages
    return (bot_id, bot_first_name, bot_last_name, bot_username,
            bot_can_join_groups, bot_can_read_all_group_messages)


prefix = ('$', '!', '.', '%', '&', ':', '|', '+', '-', '/', '~', '?')  # Все доступные префиксы бота
logs = ("<green>{time:YYYY-MM-DD HH:mm:ss}</green> <red> | </red> "
        "<blue>PRIMO-{extra[custom_variable]}</blue> <red> | </red>"
        " <red>{extra[user_var]}</red> <red> | </red><level>{message}</level>")
filtre = F.document | F.video | F.animation | F.voice | F.video_note


ban_list_id = bot_secrets.ban_list
important_adm_id = bot_secrets.important_adm_id
important_group_id = bot_secrets.important_group_id
# Сложение двух словарей
important_ids = important_adm_id.copy()
important_ids.update(important_group_id)


# Важные переменные пути
user_info_file_path = "BotInfo/user_data.txt"
log_file_path = "BotInfo/bot_log.txt"
info_file_path = "BotInfo/bot.info"
secret_file_path = "BotInfo/bot_secrets.py"

# Пути к хранению медиа
base_path = "BotFiles/BotReceivedMedia"
photo_path = "BotFiles/BotReceivedMedia/Photo"
video_path = "BotFiles/BotReceivedMedia/Video"
GIF_path = "BotFiles/BotReceivedMedia/GIF"
document_path = "BotFiles/BotReceivedMedia/Document"
videonote_path = "BotFiles/BotReceivedMedia/VideoNote"
voice_path = "BotFiles/BotReceivedMedia/Voice"
youtube_path = "BotFiles/BotReceivedMedia/Video/YouTube"
