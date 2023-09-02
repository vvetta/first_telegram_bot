import aiogram
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton

# from secret.py
from secret import API_TOKEN


# kb = ReplyKeyboardMarkup(resize_keyboard=True)
# button_help = KeyboardButton('/help')
# button_sticker = KeyboardButton('/sticker')
# button_photo = KeyboardButton('/photo')
# button_location = KeyboardButton('/location')
# kb.add(button_help).insert(button_sticker).add(button_photo).insert(button_location)


# ikb = InlineKeyboardMarkup(row_width=2)
# button_1 = InlineKeyboardButton(text='help', url='yandex.ru')
# button_2 = InlineKeyboardButton(text='sticker', url='yandex.ru')
# button_3 = InlineKeyboardButton(text='photo', url='yandex.ru')
# button_4 = InlineKeyboardButton(text='location', url='yandex.ru')
# ikb.add(button_1, button_2, button_3, button_4)


HELP_COMMAND = """
/help - список команд
/start - запуск бота
/sticker - класный стикер
/photo - фото
/location - локация
/all_methods - dir(messages)
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
    # await message.delete() # Удаляет сообщение пользователя
    
    ikb = InlineKeyboardMarkup(row_width=2)
    button_1 = InlineKeyboardButton(text='💩', callback_data='func_1')
    button_2 = InlineKeyboardButton(text='💋', callback_data='func_2')
    ikb.add(button_1, button_2)
    
    await message.answer(text='Добро пожаловать!🤡\n',
                         reply_markup=ikb)
    # await message.answer('<strong>Тут будет сообщение</strong>', parse_mode='HTML')
    

@dp.callback_query_handler()
async def callback_func(callback: aiogram.types.CallbackQuery):
    if callback.data == 'func_1':
        await callback.answer(text='Ты какашка!', show_alert=True)
    elif callback.data == 'func_2':
        await callback.answer(text='Чмок!')


@dp.message_handler(commands=['sticker'])
async def get_sticker(message: aiogram.types.Message):
    await bot.send_sticker(message.from_user.id, 
    sticker='CAACAgUAAxkBAAEKLgFk8IMUjpIbfQLp6r4nEgk0AvNQBgACGQMAAo0JiVWW-4DaQ3diujAE')
    

@dp.message_handler(commands=['photo'])
async def get_photo(message: aiogram.types.Message):
    await bot.send_photo(chat_id=message.from_user.id, 
    photo='https://w7.pngwing.com/pngs/235/163/png-transparent-ghost-drawing-halloween-ghost-pics-white-marine-mammal-fictional-character-thumbnail.png')


@dp.message_handler(commands=['location'])
async def get_location(message: aiogram.types.Message):
    await bot.send_location(chat_id=message.from_user.id, 
                            latitude=55,
                            longitude=74)
    

@dp.message_handler(commands=['all_methods'])
async def get_all_methods(message: aiogram.types.Message):
    await bot.send_message(chat_id=message.from_user.id, 
                            text=dir(message.from_user))


if __name__ == '__main__':
    aiogram.executor.start_polling(dp, on_startup=on_startup,
                                   skip_updates=True)
