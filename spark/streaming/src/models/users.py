from sqlalchemy import Column, Integer, Text
from models.base import Base


class Users(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    user_name = Column(Text, nullable=False)
    user_email = Column(Text, nullable=False, unique=True)
