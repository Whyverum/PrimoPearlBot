# BotCode/routers/common/msg_default.py
# Небольшое облегчение для команд

from loguru import logger
from BotCode.routers.downloads.download_avatar_all import download_avatar
from BotLibrary.analitics.message_to_file import write_message_to_file
from BotLibrary.analitics.user_data_to_file import write_user_info_to_file

async def msg_default(message):
    await download_avatar(message)
    await write_message_to_file(message)
    write_user_info_to_file(message.from_user)
