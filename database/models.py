import asyncpg
from typing import Optional
import os
from .db import db
from sqlalchemy import select
from database.tables import users

DATABASE_URL = os.getenv("DATABASE_URL")

async def get_user_language(user_id: int) -> str:
    query = select(users.c.language).where(users.c.user_id == user_id)
    result = await db.fetch_one(query)
    return result["language"] if result and result["language"] else "en"

async def connect_db():
    return await asyncpg.connect(DATABASE_URL)

# Получить настройки пользователя
async def get_user_settings(user_id: int) -> Optional[dict]:
    conn = await connect_db()
    row = await conn.fetchrow(
        "SELECT nickname, language FROM users WHERE user_id = $1", user_id
    )
    await conn.close()
    if row:
        return {"nickname": row["nickname"], "language": row["language"]}
    return None

# Обновить ник пользователя
async def update_nickname(user_id: int, new_nickname: str) -> None:
    conn = await connect_db()
    await conn.execute(
        "UPDATE users SET nickname = $1, last_nickname_change = NOW() WHERE user_id = $2",
        new_nickname,
        user_id
    )
    await conn.close()

# Обновить язык пользователя
async def update_language(user_id: int, new_language: str) -> None:
    conn = await connect_db()
    await conn.execute(
        "UPDATE users SET language = $1 WHERE user_id = $2", new_language, user_id
    )
    await conn.close()
