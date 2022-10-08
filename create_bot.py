from aiogram import Bot, Dispatcher
import logging
import os
import config

logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)