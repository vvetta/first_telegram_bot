from bot_files.handlers.user_handlers import register_user_handlers
from aiogram import Dispatcher, Bot, types
from dotenv import load_dotenv
# import logging
import asyncio
import os


def register_handler(dp: Dispatcher) -> None:
    register_user_handlers(dp)
    

async def main() -> None:
    load_dotenv('.env')
    
    token = os.getenv('TOKEN_API')
    bot = Bot(token)
    dp = Dispatcher(bot)
    
    register_handler(dp)
    
    try:
        await dp.start_polling()
    except Exception as _ex:
        print(_ex)
        


if __name__ == "__main__":
    asyncio.run(main())