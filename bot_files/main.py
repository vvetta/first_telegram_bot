import aiogram

# from secret.py
from secret import API_TOKEN

HELP_COMMAND = """
/help - список команд
/start - запуск бота
"""


bot = aiogram.Bot(API_TOKEN)
dp = aiogram.Dispatcher(bot=bot)


# @dp.message_handler()
# async def echo(message: aiogram.types.Message):
#     await message.answer(text=message.text) 


@dp.message_handler(commands=['help'])
async def help_command(message: aiogram.types.Message):
    await message.reply(text=HELP_COMMAND)
    
    
@dp.message_handler(commands=['start'])
async def start_command(message: aiogram.types.Message):
    await message.answer(text='Добро пожаловать!')


if __name__ == '__main__':
    aiogram.executor.start_polling(dp)
