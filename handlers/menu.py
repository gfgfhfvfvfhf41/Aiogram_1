from keyboards.keyboard_info import keyboard_for_info
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery, ReplyKeyboardMarkup, Contact, ContentType
from loader import dp, bot
from states.using import uses
from keyboards.key_back import key_for_back
from .start import started
from keyboards.keyboard_for_debugging import keyboard_for_debugging

class User:
    def __init__(self):
        self.user_id = None

users_dict = {}

@dp.message_handler(state=uses.use1)
async def menu(message: Message, state=FSMContext):
    user_id = message.from_user.id
    users_dict[user_id] = User()
    users_dict[user_id].user_id = user_id

    answer = message.text
    if answer == "/start":
        await started(message)
    elif answer == "Показать кнопки":
        await bot.send_message(users_dict[user_id].user_id, 'Выберите Ваш вопрос. Если хотите вернуться, нажмите кнопку "Назад".', reply_markup=keyboard_for_info)
        await uses.use2.set()
    elif answer == "Написать вопрос  самому":
        await bot.send_message(users_dict[user_id].user_id, 'Напишите свой вопрос. Если хотите вернуться, нажмите кнопку "Назад".', reply_markup=key_for_back)
        await uses.use3.set()
    elif answer == "debugging":
        if users_dict[user_id].user_id == 762138557:
            await bot.send_message(762138557, 'Вы перешли в Debugging меню', reply_markup=keyboard_for_debugging)
            await uses.use4.set()
        else:
            await bot.send_message(users_dict[user_id].user_id, 'Воспользуйтесь, пожалуйста, кнопками.')
    elif answer == "debugging_admin_762138557":
        await bot.send_message(users_dict[user_id].user_id, 'Вы перешли в Debugging меню', reply_markup=keyboard_for_debugging)
        await uses.use4.set()
    else:
        await bot.send_message(users_dict[user_id].user_id, 'Воспользуйтесь, пожалуйста, кнопками.')