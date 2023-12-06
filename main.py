import shutil
from aiogram import executor

from other.notify_for_admins import on_startup_notify
from other.bot_commands import set_bot_commands
from handlers import dp


async def on_startup(dispatcher):
    await on_startup_notify(dispatcher)
    await set_bot_commands(dispatcher)
    shutil.copyfile(r'data/CmpTelega3.db', r'backup_db/backup_on_startup.db')

async def on_shutdown(dispatcher):
    shutil.copyfile(r'data/CmpTelega3.db', r'backup_db/backup_on_shutdown.db')

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)


