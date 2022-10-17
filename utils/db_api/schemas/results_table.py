from sqlalchemy import Column, String, Integer, TIMESTAMP, Float

from utils.db_api.db_gino import TimedBaseModel


class ResultNeuroBet(TimedBaseModel):
    __tablename__ = 'result_neuro_bets'
    id = Column(Integer, primary_key=True)
    event_start_time = Column(TIMESTAMP)
    event_league = Column(String)
    team_1_name = Column(String)
    team_2_name = Column(String)
    first_team_percentage = Column(String)
    draw_percentage = Column(String)
    second_team_percentage = Column(String)
    event_forecast = Column(String)
    first_team_odd = Column(Float)
    draw_odd = Column(Float)
    second_team_odd = Column(Float)
    event_result = Column(String)
    # Сыграла ли ставка 0 - отменили, 1 - зашла, 2 - не зашла
    bet_played = Column(Integer, default = 0)
