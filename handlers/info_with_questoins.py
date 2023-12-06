import aiogram
import clr
import requests
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery, ReplyKeyboardMarkup, Contact, ContentType
from loader import dp, bot
from states.using import uses
from keyboards.keyboard_menu import keyboard_for_menu
from handlers.start import started
import string
from bs4 import BeautifulSoup as BS

def clean_text(text, link):
    text = text.replace("href", "\n")
    text = text.replace(u'\xa0', u' ')
    text = text.splitlines()
    b[link] = text




b = {}

def clean_text(text, link):
    text = text.replace("href", "\n")
    text = text.replace(u'\xa0', u' ')
    text = text.splitlines()
    b[link] = text



r = requests.get("https://news.rambler.ru/")
html = BS(r.text, 'lxml')
bg = html.findAll("article")

for n in bg:
    for jj in n:
        i = jj.get('href')
        clean_text(n.getText("href"), i)

#print(b)




class User:
    def __init__(self):
        self.user_id = None

clr.AddReference("D:\Build\Debug\STLib.dll")
from STLib import Main
Main.Init("D:\Sharaga_bot\CMPHandler\model.json")

users_dict = {}



@dp.message_handler(state=uses.use3)
async def info_with_que(message: Message, state=FSMContext):
    user_id = message.from_user.id
    users_dict[user_id] = User()
    users_dict[user_id].user_id = user_id
    answer = message.text
    if answer == "/start":
        await started(message)
    elif answer == "Назад":
        await bot.send_message(users_dict[user_id].user_id, 'Хорошо, Вы были перемещены в начальное меню', reply_markup=keyboard_for_menu)
        await uses.use1.set()


    elif answer == "новости" or answer == "Новости":
        for key in b:
            try:
                await bot.send_message(users_dict[user_id].user_id, f'<b>{b[key][0]}</b>\n\nКатегория: {b[key][1]}\nВремя публикации: {b[key][2]}\nКомментарии: {b[key][3]}\n\nСсылка: {key}')

                print(f"{b[key][0]}")
                print(f"Категория: {b[key][1]}")
                print(f"Время публикации: {b[key][2]}")
                print(f"Комментарии: {b[key][3]}")
                print(f"Ссылка: {key}\n")
            except IndexError:
                await bot.send_message(users_dict[user_id].user_id, f'<b>{b[key][0]}</b>\n\nКатегория: {b[key][1]}\nВремя публикации: {b[key][2]}\nКомментарии: 0\n\nСсылка: {key}')
                print(f"\n{b[key][0]}")
                print(f"Категория: {b[key][1]}")
                print(f"Время публикации: {b[key][2]}")
                print("Комментарии: нет\n")
                print(f"Ссылка: {key}")



    else:
        print(answer)
        answer = answer.translate(str.maketrans({char: " " for char in string.punctuation})).lower().split()
        answer_for_user = Main.GetAnswer(answer)

        if answer_for_user is not None:
            await bot.send_message(users_dict[user_id].user_id, f'{answer_for_user}\n\n Если хотите вернуться назад, нажмите кнопку "Назад".')
        else:
            await bot.send_message(users_dict[user_id].user_id, "Неккоретно введен вопрос, пожалуйста, попробуйте еще раз!")