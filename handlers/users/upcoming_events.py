import datetime
import zoneinfo

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.utils.markdown import hbold

from keyboards.inline.main import main_menu_keyboard, menu_one_button_keyboard
from loader import dp
from utils.db_api import neuro_football_commands
from utils.db_api.schemas.neuro_bet import NeuroBet



def create_text_method(neuro_football_bet:NeuroBet):
    text = f'''Начало в {hbold(neuro_football_bet.event_start_time.strftime('%H:%M'))} мск\n{neuro_football_bet.event_league}\n{neuro_football_bet.team_1_name} - {neuro_football_bet.team_2_name}\nПрогноз: {hbold(neuro_football_bet.event_forecast)}, КФ {hbold(neuro_football_bet.first_team_odd) if neuro_football_bet.event_forecast == 'П1'else hbold(neuro_football_bet.second_team_odd)}\nВероятность события(NeuroFootball): {hbold(neuro_football_bet.first_team_percentage) if neuro_football_bet.event_forecast == 'П1'else neuro_football_bet.second_team_percentage}\n\n'''
    return text

@dp.callback_query_handler(text='upcoming-events')
async def main_menu(call: types.CallbackQuery):
    await call.message.delete()
    current_time = datetime.datetime.now(zoneinfo.ZoneInfo("Europe/Moscow")).replace(tzinfo=None)
    result = await neuro_football_commands.get_list_upcoming_events()
    if result:
        text = ''
        amount = 0
        needed_time = None
        for x in result:
            if x.event_start_time > current_time:
                needed_time = x
                break
        for z in result:
            if z.event_start_time == needed_time.event_start_time:
                text += create_text_method(z)
                amount+=1
        end_text = f'Ближайшие события({amount}):\n\n' + text
        await call.message.answer(text=end_text, reply_markup=menu_one_button_keyboard)
