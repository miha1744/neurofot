from sqlalchemy import Column, BigInteger, String, sql
from sqlalchemy.orm import relationship
from utils.db_api.db_gino import TimedBaseModel


class Admin(TimedBaseModel):
    __tablename__ = 'admins'
    user_id = Column(BigInteger, primary_key=True)
    query: sql.Select
