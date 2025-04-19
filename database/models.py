import asyncpg
import os

DB_URL = os.getenv("DATABASE_URL")

async def get_connection():
    return await asyncpg.connect(dsn=DB_URL)

async def get_user_language(user_id: int) -> str:
    conn = await get_connection()
    row = await conn.fetchrow("SELECT language FROM users WHERE user_id = $1", user_id)
    await conn.close()
    return row["language"] if row else "en"

async def update_user_language(user_id: int, language: str):
    conn = await get_connection()
    await conn.execute("UPDATE users SET language = $1 WHERE user_id = $2", language, user_id)
    await conn.close()

async def update_user_nickname(user_id: int, nickname: str):
    conn = await get_connection()
    await conn.execute("UPDATE users SET nickname = $1 WHERE user_id = $2", nickname, user_id)
    await conn.close()

async def nickname_exists(nickname: str) -> bool:
    conn = await get_connection()
    row = await conn.fetchrow("SELECT 1 FROM users WHERE nickname = $1", nickname)
    await conn.close()
    return row is not None
