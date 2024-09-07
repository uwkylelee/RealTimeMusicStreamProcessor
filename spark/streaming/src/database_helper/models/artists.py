from sqlalchemy import Column, Integer, Text
from database_helper.models.base import Base


class Artists(Base):
    __tablename__ = 'artists'

    artist_id = Column(Integer, primary_key=True, autoincrement=True)
    artist_name = Column(Text, nullable=False, unique=True)
