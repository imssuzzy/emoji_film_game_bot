from aiogram import types
from database.manager import CategoryManager, FilmManager
from bot_utils.keybords import get_category_btns

from redis_client import redis_client
from states import UserMessageState
from aiogram.dispatcher import FSMContext

async def welcome_message(message:types.Message):
    text = """
    Привет! Давай поиграем в 'Угадай фильм по эмодзи!'. Чтобы начать игру, отправь мне сообщение 'Начать игру'.🎮🎬
    """
  
    
    await message.answer(text)

async def start_game(message:types.Message):
    text = "Выберите категорию игры:"
    user_id = message["from"].id
    data =await redis_client.get_user_data(user_id)
    if data:
        await message.answer("У вас уже имеется текущая игра. Желаете завершить игру?")
    else:
        markup = get_category_btns()
        await message.answer(text, reply_markup=markup)
    

async def start_with_category(call: types.CallbackQuery, state: FSMContext):
    user_data = await redis_client.get_user_data(call.message.chat.id)
    if user_data:
        await call.message.answer("У вас имеется активная игра, завершите игру чтобы выбрать новую категорию")
    else:
        choice = str(call.data).split("_")[1]
        data = {
            "level_choice":choice,
            "test":"test",
        }
    user_id = call.message.chat.id
    await UserMessageState.answer_text.set()
    await redis_client.cache_user_data(user_tg_id=user_id, data=data)
    await call.message.answer("Вы выбрали категорию. Игра началась...")


async def send_questions(message:types.Message, state: FSMContext):
    



async def finish_game(message:types.Message):
    user_id = message["from"].id
    await redis_client.del_user_data(user_id)
    await message.answer("Игра завершена!")
    await message.answer("Количество угаданных фильмов: 0")


async def get_movie(message:types.Message):
    films = FilmManager().get_films()
    for f in films:
        await message.answer(f"{f.emoji_text}")