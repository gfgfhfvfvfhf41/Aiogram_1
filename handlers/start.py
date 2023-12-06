import sqlite3

from aiogram import types
from aiogram.types import Message, CallbackQuery, ReplyKeyboardMarkup, Contact, ContentType
from loader import dp, bot
from other.bot_commands import set_bot_commands
from states.register_states import register
from states.using import uses
from keyboards.keyboard_menu import keyboard_for_menu

class User:
    def __init__(self):
        self.user_id = None



def check_id(ids):
    conn = sqlite3.connect('data/CmpTelega3.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id FROM Users')
    rows = cursor.fetchall()
    inside = []
    for row in rows:
        a = [*row]
        inside.append(a[0])
    conn.close()
    if ids in inside:
        return True
    else:
        return False


users_dict = {}


@dp.message_handler(commands=['start'], state=None)
async def started(message: Message, keyboard=None):
    #await set_bot_commands(dp)
    user_id = message.from_user.id
    users_dict[user_id] = User()
    users_dict[user_id].user_id = user_id

    if check_id(users_dict[user_id].user_id):
        await bot.send_message(users_dict[user_id].user_id, f"Привет, {message.from_user.first_name}.", reply_markup=keyboard_for_menu)
        await uses.use1.set()
    else:
        keyboard = types.ReplyKeyboardMarkup()
        button = types.KeyboardButton("Чтобы мы могли с тобой связаться", request_contact=True)
        keyboard.add(button)
        await bot.send_message(users_dict[user_id].user_id, 'Тык сюды...', reply_markup=keyboard)
        await register.stepr1.set()
