import aiogram

# from secret.py
from secret import API_TOKEN


bot = aiogram.Bot(API_TOKEN)
dp = aiogram.Dispatcher(bot=bot)


@dp.message_handler()
async def echo(message: aiogram.types.Message):
    await message.answer(text=message.text) 


if __name__ == '__main__':
    aiogram.executor.start_polling(dp)
