from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_main_keyboard() -> InlineKeyboardMarkup:
    
    ikb = InlineKeyboardMarkup(row_width=2)
    
    button_1 = InlineKeyboardButton(text='Да!', callback_data='func_1')
    button_2 = InlineKeyboardButton(text='Нет(', callback_data='func_2')
    
    ikb.add(button_1, button_2)
    
    return ikb
    