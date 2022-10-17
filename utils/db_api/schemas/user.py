from sqlalchemy import Column, BigInteger, String, sql
from sqlalchemy.orm import relationship
from utils.db_api.db_gino import TimedBaseModel


class User(TimedBaseModel):
    __tablename__ = 'users'
    id = Column(BigInteger, primary_key=True)
    balance = Column(BigInteger)
    subscription = Column(String)
    user_name = Column(String)
    name = Column(String(100))
    referral = Column(BigInteger)
    query: sql.Select



