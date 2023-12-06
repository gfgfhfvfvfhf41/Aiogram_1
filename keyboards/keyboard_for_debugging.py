from aiogram import types
#debugging
keyboard_for_debugging = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
del_db = types.KeyboardButton("Удалить поломанную БД")
take_db = types.KeyboardButton("Получить копию базы")
back = types.KeyboardButton("Назад")
db_start = types.KeyboardButton("Взять БД из стартового бекапа")
db_shut = types.KeyboardButton("Взять БД из конечного бекапа")
take_start = types.KeyboardButton("Получить копию стартовой базы")
take_shut = types.KeyboardButton("Получить копию конечной базы")
keyboard_for_debugging.add(del_db, take_db, db_start, db_shut, take_start, take_shut, back)