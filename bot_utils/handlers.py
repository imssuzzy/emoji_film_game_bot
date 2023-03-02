from aiogram import types
from database.manager import CategoryManager

async def welcome_message(message:types.Message):
    text = """
    Привет! Давай поиграем в 'Угадай фильм по эмодзи!'. Чтобы начать игру, отправь мне сообщение 'Начать игру'.🎮🎬
    """
    categories = CategoryManager().get_all_categories()
    markup = types.InlineKeyboardMarkup(width=1)
    for c in categories:
        markup.add(
            types.InlineKeyboardButton(c.name, callback_data=f"category_{c.id}")
        )
    
    await message.answer(text, reply_markup=markup)

