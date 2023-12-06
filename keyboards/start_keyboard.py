from aiogram import types
from loader import dp, bot

s_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
a = types.KeyboardButton("Купить игру")
b = types.KeyboardButton("Пополнить баланс")
s_keyboard.add(a, b)
