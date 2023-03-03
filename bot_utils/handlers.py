from aiogram import types
from database.manager import CategoryManager, FilmManager
from bot_utils.keybords import get_category_btns

async def welcome_message(message:types.Message):
    text = """
    Привет! Давай поиграем в 'Угадай фильм по эмодзи!'. Чтобы начать игру, отправь мне сообщение 'Начать игру'.🎮🎬
    """
  
    
    await message.answer(text)

async def start_game(message:types.Message):
    text = "Выберите категорию игры:"
    markup = get_category_btns()
    await message.answer(text, reply_markup=markup)
    

async def start_with_category(call: types.CallbackQuery):
    print(call.data)
    await call.message.answer("Вы выбрали категорию. Игра началась...")

async def get_movie(message:types.Message):
    films = FilmManager().get_films()
    for f in films:
        await message.answer(f"{f.emoji_text}")