from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.utils.markdown import hlink, hunderline, hbold

from keyboards.inline.main import menu_one_button_keyboard
from loader import dp


@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: types.Message, state: FSMContext):
    await state.reset_state()
    text = f"Привет, это {hbold('NeuroFootball')} бот ⚽\n\n" \
           f"Разработан командой программистов из Яндекса и представляет из себя самообучающуюся нейросеть класса CNN, " \
           f"основанную на модели Диксона и Коулза. " \
           f"Каждый из 5 слоев NeuroFootball обобщает и соединяет получаемые в реальном времени данные.\n\n"\
           f"🤖Нейросеть учитывает такие факторы, как: \n\n"\
           f"📊 {hunderline('Динамика команд')} (Успех команды или неудача на основе текущего выступления и силе). \n"\
           f"🏅 {hunderline('Силовой рейтинг команд')} (Учитывает силу игроков, тренера, турнирное место команды, качество игры в последних матчах). \n"\
           f"📰 {hunderline('Новости футбола')} (Трансферные новости, травмы, штрафные карточки)\n"\
           f"Проект полностью бесплатный, и создан на интузиазме. Присоединяйся к нашему {hlink('чату', url='https://t.me/neurofootball_chat')}!\n"
    await message.answer(text=text, reply_markup=menu_one_button_keyboard)
