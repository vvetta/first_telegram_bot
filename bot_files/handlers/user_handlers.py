from aiogram import types, Dispatcher
from bot_files.keyboards.user_keyboards import get_main_keyboard


async def cmd_start(message: types.Message) -> None:
    
    reply_text = 'Привет! Как твои дела?\n'
    reply_text += f'Тебя зовут - {message.from_user.first_name}, не так ли?'
    
    await message.answer (
        text=reply_text,
        reply_markup=get_main_keyboard
        )
    
    
def register_user_handlers(dp: Dispatcher) -> None:
    
    dp.register_message_handler(cmd_start, commands=['start'])
    