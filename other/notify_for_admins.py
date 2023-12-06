from aiogram import Dispatcher

admin = 762138557

async def on_startup_notify(dp: Dispatcher):
    await dp.bot.send_message(admin, "Бот запущен!")