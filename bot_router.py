from aiogram import Bot, Dispatcher

from config import TOKEN
from bot_utils import handlers as hs

bot = Bot(token=TOKEN)

dp = Dispatcher(bot)

dp.register_message_handler(hs.welcome_message, commands=['start'])
dp.register_message_handler(hs.start_game, commands=["start_game"])



dp.register_callback_query_handler(hs.start_with_category, 
lambda c: str(c.data).startswith("category_"))