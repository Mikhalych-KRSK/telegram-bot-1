from aiogram import bot, Dispatcher, executor, types
from create_bot import dp, bot
from keyboard import kb_client

#@dp.message_handler()
#async def echo(message: types.Message):
#    await message.answer(message.text)
       

#@dp.message_handler(commands=["start"])
async def process_start_command(message: types.Message):
    await message.reply("Приветствую в чатике!")
    await bot.send_message(message.from_user.id, "Теперь тебе доступны кнопки", reply_markup=kb_client)


#@dp.message_handler(commands=['Кто я?'])
async def process_question_command(message: types.Message):
    #await message.reply("Ответил в лс!")
    await bot.send_message(message.from_user.id, "Ты лох)")


async def send_cekrets_command(message: types.Message):
    await bot.send_message(message.from_user.id, "Готов?)")
    await bot.send_video(message.chat.id, open('VideoFile1.mp4', 'rb'))
    await bot.send_message(message.from_user.id, "Напиши: 'Да, конечно, 100%' или 'Нет'")
    
async def invitation(message: types.Message):
    await bot.send_message(message.from_user.id, "https://t.me/+itMNDkjlKj1iZTdi")
    
async def question_one(message: types.Message):
    await message.answer("Хороший вопрос...")
    
async def question_two(message: types.Message):
    await message.answer("У нас есть слова, которые не прошли цензуру: Путин, Z, Ян, Аниме. Список будет пополняться))")


def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(process_question_command, lambda message: "Кто я?" in message.text) 
    dp.register_message_handler(process_start_command, commands=['start'])
    dp.register_message_handler(send_cekrets_command, lambda message: "Секретик" in message.text)
    dp.register_message_handler(invitation, lambda message: "Да, конечно, 100%" in message.text)
    dp.register_message_handler(question_one, lambda message: "Как дела?" in message.text) 
    dp.register_message_handler(question_two, lambda message: "Какая цензура?" in message.text) 
