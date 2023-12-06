from aiogram import types

keyboard_for_info = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
back = types.KeyboardButton("Назад")
egor = types.KeyboardButton("Новости")
keyboard_for_info.add(egor, back)