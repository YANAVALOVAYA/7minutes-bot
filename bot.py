import logging
import openai
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# Токен бота
TOKEN = "ВАШ_ТЕЛЕГРАМ_БОТ_ТОКЕН"
OPENAI_API_KEY = "ВАШ_OPENAI_API_КЛЮЧ"

openai.api_key = OPENAI_API_KEY

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer("Привет! Я бот 7minutes. Чем могу помочь?")

executor.start_polling(dp, skip_updates=True)
