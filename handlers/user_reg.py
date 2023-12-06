import aiogram
import sqlite3
from loader import dp, bot
from aiogram.types import Message, ContentType, Contact
from aiogram.dispatcher import FSMContext
from states.register_states import register
from states.using import uses
from keyboards.keyboard_menu import keyboard_for_menu


class User_Reg:
    def __init__(self):
        self.user_id = None
        self.user_number = None
        self.user_tag = None


users_dict = {}


@dp.message_handler(content_types=ContentType.CONTACT, state=register.stepr1)
async def test(message: Message, states=FSMContext):
    user_id = message.from_user.id
    users_dict[user_id] = User_Reg()
    users_dict[user_id].user_id = user_id
    users_dict[user_id].user_number = message.contact.phone_number
    users_dict[user_id].user_tag = message.from_user.username

    conn = sqlite3.connect('data/CmpTelega3.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Users (id, Phone, tag) VALUES(?, ?, ?)",
                   (users_dict[user_id].user_id, users_dict[user_id].user_number, users_dict[user_id].user_tag))

    await bot.send_message(users_dict[user_id].user_id,
                           f'Ваш номер: {users_dict[user_id].user_number}\nВаш ID: {users_dict[user_id].user_id}',
                           reply_markup=keyboard_for_menu)
    await bot.send_message(762138557,
                           f'ID юзера: {users_dict[user_id].user_id}, Номер юзера {users_dict[user_id].user_number}, Тег юзера {users_dict[user_id].user_tag}')
    await uses.use1.set()
    conn.commit()
    conn.close()
# aiogram.types.ReplyKeyboardRemove()
