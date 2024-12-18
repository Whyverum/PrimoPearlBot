from random import randint

from aiogram import Router, F
from aiogram.types import CallbackQuery
from keyboards.inline_kb.actor_kb import ButtonInl

router = Router(name="actor_kb_cb_router")

@router.callback_query(F.data == ButtonInl.random_site_cbd)
async def random_site_cb(callback_query: CallbackQuery):
    bot_me = await callback_query.bot.me()
    await callback_query.answer(
        url=f"t.me/{bot_me.username}?start={randint(1, 500)}"
    )


@router.callback_query(F.data == ButtonInl.random_num_dice_cbd)
async def random_num_dice_cb(callback_query: CallbackQuery):
    await callback_query.answer(
        text = f"Твое рандомное число: {randint(1, 21)}",
        cache_time=1,
    )


@router.callback_query(F.data == ButtonInl.random_num_modal_cdb)
async def random_num_dice_modal_cb(callback_query: CallbackQuery):
    await callback_query.answer(
        text = f"Членов в жопе у Степана: {randint(1, 2200)}",
        show_alert=True,
    )