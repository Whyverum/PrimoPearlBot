# BotCode/routers/callback_handlers/randnum_kb_cb.py
# Обработчик запросов в команде /randnum
import asyncio
from random import randint
from aiogram import Router, F
from aiogram.types import CallbackQuery
from BotLibrary import ikb
from BotCode.keyboards.inline_kb.randnum_kb import ButtonInl, get_randnum_kb

# Создание роутера и настройка экспорта модулей
__all__ = ("router",)
router = Router(name="randnum_kb_cb")


# Тестирование редактирования сообщения
@router.callback_query(F.data == ButtonInl.mark_cbd)
async def random_site_cb(callback_query: CallbackQuery):
    await callback_query.answer()

    # Новый текст и клавиатура
    new_text = f"Какая оценка у тебя будет сегодня: {randint(1, 5)}"
    new_reply_markup = ikb.as_markup()  # Обновленная клавиатура

    # Проверка, отличается ли текущее сообщение от нового
    if callback_query.message.text != new_text or callback_query.message.reply_markup != new_reply_markup:
        # Добавляем задержку, если необходимо
        await asyncio.sleep(0.5)  # Задержка 0.5 секунд

        # Редактируем сообщение и обновляем клавиатуру
        await callback_query.message.edit_text(
            text=new_text,
            reply_markup=new_reply_markup,  # Обновляем клавиатуру
        )
