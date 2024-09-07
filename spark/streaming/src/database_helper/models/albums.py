from sqlalchemy import Column, Integer, Text
from database_helper.models.base import Base


class Albums(Base):
    __tablename__ = 'albums'

    album_id = Column(Integer, primary_key=True, autoincrement=True)
    album_name = Column(Text, nullable=False, unique=True)
