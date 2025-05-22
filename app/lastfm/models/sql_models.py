from sqlalchemy import Column, String, Integer
from app.core.database import Base

class ScrobbleORM(Base):
    # TODO: will need multiple relational tables
    __tablename__ = "scrobbles"

    # TODO: add multiple tables, log album covers, similar tracks, playcount, top tags, etc.
    # Track object methods to consider:
    # - track.get_cover_image(), track.get_duration(), track.get_listener_count(), track.get_playcount()
    # - track.get_similar(), track.get_top_tags(), track.get_wiki_content() 
    # Artist object methods to consider:
    # - artist.get_bio(), artist.get_top_albums(), artist.get_top_tracks()
    id = Column(Integer, primary_key=True, index=True)
    track = Column(String)
    artist = Column(String)
    album = Column(String, nullable=True)
    playback_date = Column(String)
    timestamp = Column(String)

