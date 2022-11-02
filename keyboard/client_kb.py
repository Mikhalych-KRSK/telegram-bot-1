from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

b1 = KeyboardButton("/start")
b2 = KeyboardButton("Кто я?")
#b3 = KeyboardButton("Секретик")
b4 = KeyboardButton("Загадка")

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)#, one_time_keyboard=True)

#reply_markup=ReplyKeyboardRemove удаление клавиатуры

#kb_client.add(b1).add(b2) или
kb_client.row(b1, b2)#.add(b4)