from aiogram import types

key_for_back = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
wallet = types.KeyboardButton("Назад")
key_for_back.add(wallet)