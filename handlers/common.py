import os, json, string
from aiogram import Bot, Dispatcher, executor, types
from create_bot import dp


#@dp.message(content_types=types.ContentType.NEW_CHAT_MEMBERS)
async def somebody_added(message: types.Message):
    for user in message.new_chat_members:
        # проперти full_name берёт сразу имя И фамилию 
        await message.reply(f"Привет, {user.full_name}")


#проверка на цензуру
#@dp.message_handler()
async def filter_messages(message: types.Message):
    if {i.lower().translate(str.maketrans("", "", string.punctuation)) for i in message.text.split(" ")}\
        .intersection(set(json.load(open("XXX.json")))) != set():
        await message.reply("Я удалил твоё сообщение! Следи за языком🤢")
        await message.delete()

def register_handlers_common(dp : Dispatcher):
    dp.register_message_handler(filter_messages)
    dp.register_message_handler(somebody_added, content_types=types.ContentType.NEW_CHAT_MEMBERS)