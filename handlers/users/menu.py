from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from keyboards.inline.main import main_menu_keyboard
from loader import dp


@dp.callback_query_handler(text='menu')
async def main_menu(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer(text='Меню NeuroFootball', reply_markup=main_menu_keyboard)



@dp.message_handler(Command('menu'), state='*')
async def command_main_menu(message: types.Message, state: FSMContext):
    await state.reset_state()
    await message.answer(text='Меню NeuroFootball',reply_markup=main_menu_keyboard)
