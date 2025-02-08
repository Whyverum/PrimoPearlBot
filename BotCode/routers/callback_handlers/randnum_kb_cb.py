# BotCode/routers/callback_handlers/randnum_kb_cb.py
# Обработчик запросов в команде /randnum

from random import randint
from aiogram import Router, F
from aiogram.types import CallbackQuery
from BotCode.keyboards.inline_kb.randnum_kb import ButtonInl, get_randnum_kb

# Создание роутера и настройка экспорта модулей
__all__ = ("router",)
router = Router(name="randnum_kb_cb_router")


# Тестирование редактирования сообщения
@router.callback_query(F.data == ButtonInl.mark_cbd)
async def random_site_cb(callback_query: CallbackQuery):
    await callback_query.answer()

    # Новый текст и клавиатура
    new_text = f"Какая оценка у тебя будет сегодня: {randint(1, 5)}"
    new_reply_markup = get_randnum_kb("Получить ответ от Таро")

    # Текущий текст и клавиатура
    current_text = callback_query.message.text
    current_reply_markup = callback_query.message.reply_markup

    # Проверяем, отличаются ли текст и клавиатура
    if current_text != new_text or current_reply_markup != new_reply_markup:
        await callback_query.message.edit_text(
            text=new_text,
            reply_markup=new_reply_markup,
        )
