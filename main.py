import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties

from config import BOT_TOKEN
from handlers import register_main_menu, register_settings
from middlewares.language_middleware import LanguageMiddleware

logging.basicConfig(level=logging.INFO)

async def main():
    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher(storage=MemoryStorage())

    # Middleware для языка
    dp.message.middleware.register(LanguageMiddleware())

    # Регистрация хендлеров
    register_main_menu(dp)
    register_settings(dp)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
