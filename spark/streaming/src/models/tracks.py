from sqlalchemy import Column, Integer, Text, BigInteger, ARRAY, ForeignKey
from models.base import Base


class Tracks(Base):
    __tablename__ = 'tracks'

    track_id = Column(Integer, primary_key=True, autoincrement=True)
    track_name = Column(Text, nullable=False)
    artist_id_array = Column(ARRAY(Integer))  # Foreign Key-like for Artists
    album_id = Column(Integer, ForeignKey('albums.album_id'), nullable=False)
    genre = Column(Text)
    popularity = Column(BigInteger)
    duration_ms = Column(BigInteger)
