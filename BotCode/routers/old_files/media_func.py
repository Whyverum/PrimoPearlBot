# media_func.py

from re import Match
from aiogram import Router, F, types
from magic_filter import RegexpMode
from settings import *


router = Router(name="media_func")


# @router.message(F.photo, ~F.caption)
async def handle_photo_wo_caption(message: types.Message):
    caption = f"Простите, я не могу это увидеть. Вы можете описать что это?"
    await message.reply_photo(
        photo=message.photo[-1].file_id,
        caption=caption,
    )


# @router.message(F.photo, F.caption.contains("please"))
async def handle_photo_with_please_caption(message: types.Message):
    await message.reply(f"Простите, я не могу это увидеть.")


# @router.message(any_media_filter, ~F.caption)
async def handle_any_media_wo_caption(message: types.Message):
    if message.document:
        await message.reply_document(
            document=message.document.file_id,
        )
    elif message.video:
        await message.reply_video(
            video=message.video.file_id,
        )
    else:
        await message.reply(f"Я не могу это увидеть.")


# @router.message(any_media_filter, F.caption)
async def handle_any_media_w_caption(message: types.Message):
    await message.reply(f"Что-то на медиа. Твой текст: {message.caption!r}")


# Использование регулярных функций
@router.message(F.from_user.id.in_(config.ListId.adm_list_id), F.text.regexp(r"(\d+)", mode=RegexpMode.MATCH).as_("code"))
async def handle_code(message: types.Message, code: Match[str]):
    await message.reply(f"Ваш код: {code.group()}")
