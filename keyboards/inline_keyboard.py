from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

buttons = [
    InlineKeyboardButton(text="Предыдущая", callback_data="past"),
    InlineKeyboardButton(text="Следующая", callback_data="next"),
    InlineKeyboardButton(text="Назад", callback_data="back"),
    InlineKeyboardButton(text="Перезапустить бота", callback_data="restart"),
]
inline_key = InlineKeyboardMarkup(row_width=2)
inline_key.add(*buttons)


inline_back = InlineKeyboardMarkup(row_width=2)
back = InlineKeyboardButton(text="Назад", callback_data="back")
inline_back.add(back)

inline_start = InlineKeyboardMarkup(row_width=2)
back = InlineKeyboardButton(text="Назад", callback_data="back")
start = InlineKeyboardButton(text="Смотреть новости", callback_data="start")
inline_start.add(start, back)