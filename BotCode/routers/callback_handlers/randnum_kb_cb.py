# BotCode/routers/callback_handlers/randnum_kb_cb.py
# Обработчик запросов в команде /randnum

from random import randint
from aiogram import Router, F
from aiogram.types import CallbackQuery

from BotLibrary import ikb
from BotCode.keyboards.inline_kb.randnum_kb import ButtonInl

# Создание роутера и настройка экспорта модулей
__all__ = ("router",)
router = Router(name="randnum_kb_cb")


# Тестирование редактирования сообщения
@router.callback_query(F.data == ButtonInl.mark_cbd)
async def random_site_cb(callback_query: CallbackQuery):
    await callback_query.answer()

    # Редактируем сообщение и обновляем клавиатуру
    await callback_query.message.edit_text(
        text=f"Какая оценка у тебя будет сегодня: {randint(1, 5)}",
        reply_markup=ikb.as_markup(),  # Обновляем клавиатуру
    )
