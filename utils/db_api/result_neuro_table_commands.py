import datetime

from asyncpg import UniqueViolationError

from utils.db_api.db_gino import db
from utils.db_api.schemas.neuro_bet import NeuroBet
from utils.db_api.schemas.results_table import ResultNeuroBet
from sqlalchemy import and_




# Команды связанные с юзером
async def add_result_neurofootball_bet(event_start_time, event_league, team_1_name,
                             team_2_name, first_team_percentage, draw_percentage,
                             second_team_percentage, event_forecast,first_team_odd,
                             draw_odd, second_team_odd,event_result, bet_played: int):
    # Добавить нейроставку
    try:
        result_neuro_bet = ResultNeuroBet(id=await id_result_neurofootball_bet(), event_start_time=event_start_time, event_league=event_league, team_1_name=team_1_name,
                             team_2_name=team_2_name, first_team_percentage=first_team_percentage, draw_percentage=draw_percentage,
                             second_team_percentage=second_team_percentage, event_forecast=event_forecast,first_team_odd=first_team_odd,
                             draw_odd=draw_odd, second_team_odd=second_team_odd,event_result=event_result, bet_played= bet_played)
        await result_neuro_bet.create()

    except UniqueViolationError:
        pass


async def select_all_result_neuro_football():
    # Возвращает всех пользователей
    neuro_bets = await ResultNeuroBet.query.gino.all()
    return neuro_bets



async def id_result_neurofootball_bet():
    # Возвращает id инвойса
    id = await db.func.max(ResultNeuroBet.id).gino.scalar()
    if id is not None:
        return id + 1
    else:
        return 0
