from aiogram import types
from database.manager import CategoryManager

async def welcome_message(message:types.Message):
    text = """
    Привет! Давай поиграем в 'Угадай фильм по эмодзи!'. Чтобы начать игру, отправь мне сообщение 'Начать игру'.🎮🎬
    """
    categories = CategoryManager().get_all_categories()
    for c in categories:
        await message.answer(c.name)
    
    await message.answer(text)

