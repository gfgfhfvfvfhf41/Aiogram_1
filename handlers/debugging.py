import shutil
import sqlite3
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from keyboards.keyboard_menu import keyboard_for_menu
from loader import dp, bot
from states.using import uses
from .start import started

class User:
    def __init__(self):
        self.user_id = None
users_dict = {}

async def del_db(id):
    conn = sqlite3.connect('data/CmpTelega3.db')
    c = conn.cursor()
    c.execute('DELETE FROM Users;')
    conn.commit()
    conn.close()
    await bot.send_message(id, 'Успешно удалено.')

@dp.message_handler(state=uses.use4)
async def debug(message: Message, state=FSMContext):
    user_id = message.from_user.id
    users_dict[user_id] = User()
    users_dict[user_id].user_id = user_id
    answer = message.text
    if answer == "Удалить поломанную БД":
        await message.reply_document(open('data/CmpTelega3.db', 'rb'))
        await del_db(users_dict[user_id].user_id)
    elif answer == "Получить копию базы":
        await message.reply_document(open('data/CmpTelega3.db', 'rb'))
    elif answer == "Взять БД из стартового бекапа":
        shutil.copyfile(r'backup_db/backup_on_startup.db', r'data/CmpTelega3.db')
        await message.reply_document(open('data/CmpTelega3.db', 'rb'))
        await bot.send_message(users_dict[user_id].user_id, "Выполнено")
    elif answer == "Взять БД из конечного бекапа":
        shutil.copyfile(r'backup_db/backup_on_shutdown.db', r'data/CmpTelega3.db')
        await message.reply_document(open('data/CmpTelega3.db', 'rb'))
        await bot.send_message(users_dict[user_id].user_id, "Выполнено")
    elif answer == "Получить копию конечной базы":
        await message.reply_document(open('backup_db/backup_on_shutdown.db', 'rb'))
    elif answer == "Получить копию стартовой базы":
        await message.reply_document(open('backup_db/backup_on_startup.db', 'rb'))
    elif answer == "Назад":
        await bot.send_message(users_dict[user_id].user_id, 'Хорошо, Вы были перемещены в начальное меню', reply_markup=keyboard_for_menu)
        await uses.use1.set()
    elif answer == "/start":
        await started(message)