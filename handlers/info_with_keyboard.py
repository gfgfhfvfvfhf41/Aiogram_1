import aiogram
import requests
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery, ReplyKeyboardMarkup, Contact, ContentType
from keyboards.keyboard_menu import keyboard_for_menu
from loader import dp, bot
from states.using import uses
from states.inline_states import inl
from handlers.start import started
from bs4 import BeautifulSoup as BS
from keyboards.inline_keyboard import inline_key, inline_back, inline_start
from .start import started

class User:
    def __init__(self):
        self.user_id = None
        self.iter = None
        self.keys = []
        self.chat_id = None
        self.message_id = None

b = {}

def clean_text(text, link):
    text = text.replace("href", "\n")
    text = text.replace(u'\xa0', u' ')
    text = text.splitlines()
    b[link] = text





users_dict = {}

async def egor_idet_nahuy():
    await bot.send_message(844980528, "Надыр, иди нахуй")


async def pars(user_id, iter):
    try:
        await bot.edit_message_text(f'<b>{b[users_dict[user_id].keys[iter]][0]}</b>\n\nКатегория: {b[users_dict[user_id].keys[iter]][1]}\nВремя публикации: {b[users_dict[user_id].keys[iter]][2]}\nКомментарии: {b[users_dict[user_id].keys[iter]][3]}\n\nСсылка: {users_dict[user_id].keys[iter]}', users_dict[user_id].chat_id, users_dict[user_id].message_id, reply_markup=inline_key)
        await inl.inl1.set()
        # print(f"{b[iter][0]}")
        # print(f"Категория: {b[iter][1]}")
        # print(f"Время публикации: {b[iter][2]}")
        # print(f"Комментарии: {b[iter][3]}")
        # print(f"Ссылка: {iter}\n")
    except IndexError:
        try:
            await bot.edit_message_text(f'<b>{b[users_dict[user_id].keys[iter]][0]}</b>\n\nКатегория: {b[users_dict[user_id].keys[iter]][1]}\nВремя публикации: {b[users_dict[user_id].keys[iter]][2]}\nКомментарии: 0\n\nСсылка: {users_dict[user_id].keys[iter]}', users_dict[user_id].chat_id, users_dict[user_id].message_id, reply_markup=inline_key)
        # print(f"\n{b[iter][0]}")
        # print(f"Категория: {b[iter][1]}")
        # print(f"Время публикации: {b[iter][2]}")
        # print("Комментарии: нет\n")
        # print(f"Ссылка: {iter}")
        except IndexError:
            await bot.send_message(users_dict[user_id].user_id, f'<b>К сожалению, больше нет свежих новостей</b>', reply_markup=inline_back)
            await inl.inl1.set()



@dp.message_handler(state=uses.use2)
async def info_with_key(message: Message, state=FSMContext):
    user_id = message.from_user.id
    users_dict[user_id] = User()
    users_dict[user_id].user_id = user_id
    answer = message.text
    print(answer)
    if answer == "Нахуй Надыра":
        await egor_idet_nahuy()
        await bot.send_message(users_dict[user_id].user_id, 'Вы послали Надыра нахуй')
    elif answer == "/start":
        await started(message)
    elif answer == "Назад":
        await bot.send_message(users_dict[user_id].user_id, 'Хорошо, Вы были перемещены в начальное меню', reply_markup=keyboard_for_menu)
        await uses.use1.set()
    elif answer == "Новости":
        users_dict[user_id].iter = 0
        r = requests.get("https://news.rambler.ru/")
        html = BS(r.text, 'lxml')
        bg = html.findAll("article")
        for n in bg:
            for jj in n:
                i = jj.get('href')
                clean_text(n.getText("href"), i)
        for key in b:
            users_dict[user_id].keys.append(key)


        #await bot.send_message(users_dict[user_id].user_id, 'Вы были перемещены в меню новостей', reply_markup=aiogram.types.ReplyKeyboardRemove())
        users_dict[user_id].iter = users_dict[user_id].iter + 1
        msg = await bot.send_message(users_dict[user_id].user_id, f'<b>{b[users_dict[user_id].keys[users_dict[user_id].iter]][0]}</b>\n\nКатегория: {b[users_dict[user_id].keys[users_dict[user_id].iter]][1]}\nВремя публикации: {b[users_dict[user_id].keys[users_dict[user_id].iter]][2]}\nКомментарии: 0\n\nСсылка: {users_dict[user_id].keys[users_dict[user_id].iter]}', reply_markup=inline_key)
        users_dict[user_id].message_id = msg.message_id
        users_dict[user_id].chat_id = msg.chat.id
        await inl.inl1.set()


@dp.callback_query_handler(state=inl.inl1)
async def kall(call: CallbackQuery):
    user_id = call.from_user.id
    print(users_dict[user_id].message_id + 1)
    if call.data == "next":
        users_dict[user_id].iter = users_dict[user_id].iter + 1
        await pars(user_id, users_dict[user_id].iter)
    elif call.data == "past":
        users_dict[user_id].iter = users_dict[user_id].iter - 1
        await pars(user_id, users_dict[user_id].iter)
    elif call.data == "back":
        await bot.send_message(users_dict[user_id].user_id, 'Хорошо, Вы были перемещены в начальное меню', reply_markup=keyboard_for_menu)
        await uses.use1.set()
    elif call.data == "restart":
        # async def del_bot_commands(dp):
        #     await dp.bot.set_my_commands(
        #         [
        #         ]
        #     )
        # await del_bot_commands(dp)
        await started(call)


















    # else:
    #     await bot.send_message(users_dict[user_id].user_id, 'В этом режиме я реагирую только на кнопки. Если хотите вернуться и выбрать режим, нажмите кнопку "Назад".')
    #     print(answer)



# def process_select_test(message):
#     markup = telebot.types.InlineKeyboardMarkup()
#
#     for x in json.loads(users_dict[message.from_user.id].lhandler.GetRecomendation()):
#         markup.add(telebot.types.InlineKeyboardButton(text = x["title"], callback_data = x["title"]))