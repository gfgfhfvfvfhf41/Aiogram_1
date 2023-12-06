from aiogram import types
from loader import dp, bot

keyboard_for_menu = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
buy_game = types.KeyboardButton("Показать кнопки")
wallet = types.KeyboardButton("Написать вопрос  самому")
keyboard_for_menu.add(buy_game, wallet)