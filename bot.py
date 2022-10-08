from sqlalchemy import intersect
import config
from aiogram import executor, types
from create_bot import dp
from handlers import client, admin, common

client.register_handlers_client(dp)
common.register_handlers_common(dp)



async def on_startup(_):
    print("-    __Bot online__    ")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
    