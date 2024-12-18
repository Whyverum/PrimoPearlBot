# MySQL/db.py
# Подключение базы данных   (в разработке)

import aiomysql

# Настройка экспорта модулей и логирования
__all__ = ("connect_db", "execute_query")


# Функция подключение к базе данных     (в разработке)
async def connect_db():
    return await aiomysql.connect(host='your_host',
                                  user='your_user',
                                  password='your_password',
                                  db='your_database',
                                  charset='utf8mb4',
                                  cursorclass=aiomysql.cursors.DictCursor)


# Функция выполнения запросов к БД      (в разработке)
async def execute_query(conn, query):
    async with conn.cursor() as cur:
        await cur.execute(query)
        return await cur.fetchall()

