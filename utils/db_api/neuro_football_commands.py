import datetime

from asyncpg import UniqueViolationError

from utils.db_api.db_gino import db
from utils.db_api.schemas.neuro_bet import NeuroBet
from sqlalchemy import and_

# __tablename__ = 'neuro_bets'
# id = Column(Integer, primary_key=True)
# event_start_time = Column(TIMESTAMP)
# event_league = Column(String)
# team_1_name = Column(String)
# team_2_name = Column(String)
# first_team_percentage = Column(String)
# draw_percentage = Column(String)
# second_team_percentage = Column(String)
# event_forecast = Column(String)
# first_team_odd = Column(Float)
# draw_odd = Column(Float)
# second_team_odd = Column(Float)
# event_result = Column(String)
# unique_event = Column()


# Команды связанные с юзером
async def add_neurofootball_bet(event_start_time: datetime.datetime, event_league: str, team_1_name: str, team_2_name: str,
                                first_team_percentage: str, draw_percentage: str,second_team_percentage:str,
                                event_forecast:str,first_team_odd:float, draw_odd: float, second_team_odd:float, event_result:str):
    # Добавить нейроставку
    try:
        neuro_bet = NeuroBet(id=await id_neurofootball_bet(), event_start_time=event_start_time, event_league=event_league, team_1_name=team_1_name,
                             team_2_name=team_2_name, first_team_percentage=first_team_percentage, draw_percentage=draw_percentage,
                             second_team_percentage=second_team_percentage, event_forecast=event_forecast,first_team_odd=first_team_odd,
                             draw_odd=draw_odd, second_team_odd=second_team_odd,event_result=event_result)
        await neuro_bet.create()

    except UniqueViolationError:
        pass


async def select_all_neurofootball():
    # Возвращает всех пользователей
    neuro_bets = await NeuroBet.query.gino.all()
    return neuro_bets



async def id_neurofootball_bet():
    # Возвращает id инвойса
    id = await db.func.max(NeuroBet.id).gino.scalar()
    if id is not None:
        return id + 1
    else:
        return 0


async def check_neurobet(time, team_1_name, team_2_name) -> NeuroBet:
    neuro_bet = await NeuroBet.query.where(and_(NeuroBet.event_start_time == time,NeuroBet.team_2_name == team_2_name,
                              NeuroBet.team_1_name == team_1_name)).gino.first()
    return neuro_bet



async def delete_neurobet(bet_id):
    await NeuroBet.delete.where(NeuroBet.id== bet_id).gino.status()



async def get_list_upcoming_events():
    all_list = await db.all(NeuroBet.query)
    if all_list:
        return sorted(all_list, key=lambda x: x.event_start_time)

