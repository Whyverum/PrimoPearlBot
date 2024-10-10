# db.py

import aiomysql


async def connect_db():
    return await aiomysql.connect(host='your_host',
                                  user='your_user',
                                  password='your_password',
                                  db='your_database',
                                  charset='utf8mb4',
                                  cursorclass=aiomysql.cursors.DictCursor)


async def execute_query(conn, query):
    async with conn.cursor() as cur:
        await cur.execute(query)
        return await cur.fetchall()

