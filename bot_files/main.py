import aiogram

# from secret.py
from secret import API_TOKEN

HELP_COMMAND = """
/help - список команд
/start - запуск бота
/sticker - класный стикер
"""


bot = aiogram.Bot(API_TOKEN)
dp = aiogram.Dispatcher(bot=bot)


async def on_startup(_):
    print('Бот был успешно запущен!')


# @dp.message_handler()
# async def echo(message: aiogram.types.Message):
#     await message.answer(text=message.text) 


@dp.message_handler(commands=['help'])
async def help_command(message: aiogram.types.Message):
    await message.reply(text=HELP_COMMAND) # reply - ответ на сообщение пользователя
    
    
@dp.message_handler(commands=['start'])
async def start_command(message: aiogram.types.Message):
    await message.answer(text='Добро пожаловать!🤡\n'
                                'Список команд бота: \n')
    await message.answer(text=HELP_COMMAND)
    # await message.delete() # Удаляет сообщение пользователя
    # await message.answer('<strong>Тут будет сообщение</strong>', parse_mode='HTML')


@dp.message_handler(commands=['sticker'])
async def get_sticker(message: aiogram.types.Message):
    await bot.send_sticker(message.from_user.id, 
    sticker='CAACAgUAAxkBAAEKLgFk8IMUjpIbfQLp6r4nEgk0AvNQBgACGQMAAo0JiVWW-4DaQ3diujAE')


if __name__ == '__main__':
    aiogram.executor.start_polling(dp, on_startup=on_startup)
