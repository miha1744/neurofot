from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from keyboards.inline.main import menu_one_button_keyboard
from loader import dp
from utils.parser.parser_scheduler import pars_schedule


@dp.message_handler(Command('startpars'), state='*')
async def start_parsing(message: types.Message, state: FSMContext):
    await message.answer(text="Парсниг пошел", reply_markup=menu_one_button_keyboard)
    await pars_schedule()
    await message.answer(text="Парсинг завершен", reply_markup=menu_one_button_keyboard)
