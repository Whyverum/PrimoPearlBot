# regular_handlers.py

from aiogram import F, types, Router
from magic_filter import RegexpMode
from re import Match

from settings.configs import config
from settings import write_message_to_file
from settings import write_user_info_to_file

router = Router(name="regular_handlers")


# Хэндлер на цифирный код
@router.message(
    F.from_user.id.in_(config.ListId.adm_list_id),
    F.text.regexp(r"(\d+)", mode=RegexpMode.MATCH).as_("code"),
)
async def handle_code(message: types.Message, code: Match[str]):
    await message.reply(f"Your code: {code.group()}")
    await write_user_info_to_file(message.from_user)
    await write_message_to_file(message)
    return f"Цифирный код"
