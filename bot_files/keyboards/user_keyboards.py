from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_main_keyboard() -> InlineKeyboardMarkup:
    
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton('Да!', callback_data='func_1')],
        [InlineKeyboardButton('Нет(', callback_data='func_2')]
    ], row_width=2)

    
    return ikb
    