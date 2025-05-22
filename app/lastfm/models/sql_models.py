from sqlalchemy import Column, String, Integer, DateTime
from app.core.database import Base

class ScrobbleORM(Base):
    # TODO: will need multiple relational tables
    __tablename__ = "scrobbles"

    id = Column(Integer, primary_key=True, index=True)
    track = Column(String)
    artist = Column(String)
    album = Column(String, nullable=True)
    playback_date = Column(DateTime)
    timestamp = Column(DateTime)

