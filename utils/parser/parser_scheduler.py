from aiogram.utils.markdown import hbold

from data.config import NEUROFOOTBALL_CHAT_ID
from utils.db_api import neuro_football_commands, result_neuro_table_commands
from utils.db_api.schemas import neuro_bet
from utils.db_api.schemas.neuro_bet import NeuroBet
from utils.parser.parser import create_df_robobet
from loader import dp



async def create_channel_msg(neuro_football_bet: NeuroBet, result: int):
    text = f'''{neuro_football_bet.event_league}\n{neuro_football_bet.team_1_name} - {neuro_football_bet.team_2_name}\nПрогноз: {hbold(neuro_football_bet.event_forecast)}, КФ {hbold(neuro_football_bet.first_team_odd) if neuro_football_bet.event_forecast == 'П1'else hbold(neuro_football_bet.second_team_odd)}\nВероятность победы(NeuroFootball): {hbold(neuro_football_bet.first_team_percentage) if neuro_football_bet.event_forecast == 'П1'else neuro_football_bet.second_team_percentage}\n\n'''
    final_text = ''
    if result == 0:
        final_text = hbold('СОБЫТИЕОТМЕНЕНО') + '\n' + text
    if result == 1:
        final_text = f"✅✅✅{hbold('СТАВКА ЗАШЛА')}✅✅✅" + '\n' + text
    if result == 2:
        final_text = f"🚫🚫🚫{hbold('СТАВКА НЕ ЗАШЛА')}🚫🚫🚫" + '\n' + text
    await dp.bot.send_message(chat_id=NEUROFOOTBALL_CHAT_ID, text =final_text)



async def sort_criteria(value):
    if value[-1] == '- : -':
        if value[7] == 'П1':
            if value[8] > 1.7:
                neuro_football_bet = await neuro_football_commands.check_neurobet(value[0], value[2], value[3])
                if neuro_football_bet:
                    return
                await neuro_football_commands.add_neurofootball_bet(*value)
        if value[7] == 'П2':
            if value[10] > 1.7:
                neuro_football_bet = await neuro_football_commands.check_neurobet(value[0], value[2], value[3])
                if neuro_football_bet:
                    return
                await neuro_football_commands.add_neurofootball_bet(*value)
    elif value[-1] == 'отм':
        neuro_football_bet = await neuro_football_commands.check_neurobet(value[0],value[2], value[3])
        if neuro_football_bet:
            await result_neuro_table_commands.add_result_neurofootball_bet(neuro_football_bet,value[-1], 0)
            await neuro_football_commands.delete_neurobet(neuro_football_bet.id)
            await create_channel_msg(neuro_football_bet, 0)
    else:
        neuro_football_bet = await neuro_football_commands.check_neurobet(value[0],value[2],value[3])
        if neuro_football_bet:
            actual_result = value[-1].split(':')
            if int(actual_result[0]) > int(actual_result[1]) and neuro_football_bet.event_forecast == 'П1':
                await result_neuro_table_commands.add_result_neurofootball_bet(neuro_football_bet,value[-1],1)
                await create_channel_msg(neuro_football_bet, 1)
            elif int(actual_result[0]) < int(actual_result[1]) and neuro_football_bet.event_forecast == 'П2':
                await result_neuro_table_commands.add_result_neurofootball_bet(neuro_football_bet,value[-1],1)
                await create_channel_msg(neuro_football_bet, 1)
            else:
                await result_neuro_table_commands.add_result_neurofootball_bet(neuro_football_bet,value[-1],2)
                await create_channel_msg(neuro_football_bet,2)
            await neuro_football_commands.delete_neurobet(neuro_football_bet.id)


async def pars_schedule():
    values = create_df_robobet()
    for value in values:
        await sort_criteria(value)
