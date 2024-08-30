from sqlalchemy import Column, Integer, ForeignKey, DateTime
from models.base import Base


class TrackStreamLog(Base):
    __tablename__ = 'track_stream_log'

    user_id = Column(Integer, ForeignKey('users.user_id'), primary_key=True)
    track_id = Column(Integer, ForeignKey('tracks.track_id'), primary_key=True)
    created_timestamp = Column(DateTime, nullable=False)