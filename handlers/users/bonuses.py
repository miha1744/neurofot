from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from keyboards.inline.main import main_menu_keyboard, menu_one_button_keyboard
from loader import dp


@dp.callback_query_handler(text='bonuses')
async def main_menu(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer(text='Здесь скоро будут бонусы!', reply_markup=menu_one_button_keyboard)
