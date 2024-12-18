# BotCode/routers/inline/posts_inline.py
# Создание красивых постов по вкусу (в разработке)

import hashlib
import uuid
from aiogram import Router, types

# Настройка экспорта модулей и роутера
__all__ = ("router", "ad_post")
router = Router(name="media_func")


@router.inline_query()
async def ad_post(query: types.InlineQuery):
    # Получаем строку запроса или задаем дефолтное значение
    text = query.query or "echo"

    # Создаем описание и ссылку
    response_text = "Привет, я Бот! Хотите со мной поиграть? Это кстати реклама новой трассы от Финаки!"
    link = f"https://ru.wikipedia.org/wiki/{text}"

    # Используем uuid для уникального ID результата
    result_id = str(uuid.uuid5(uuid.NAMESPACE_DNS, text))

    # Создаем Inline Query Result Article
    articles = [
        types.InlineQueryResultArticle(
            id=result_id,
            title='Cтaтья Wikipedia:',
            url=link,
            input_message_content=types.InputTextMessageContent(message_text=link),
            description=response_text  # Описание для пользователя
        )
    ]

    # Отправляем результат на inline-запрос
    await query.answer(articles, cache_time=1, is_personal=True)
