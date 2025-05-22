from pydantic import BaseModel, field_serializer
from typing import Optional
from datetime import datetime

from app.core.datetime_utils import LASTFM_DATETIME_FORMAT

class ScrobbleTransfer(BaseModel):
    track: str
    artist: str
    album: Optional[str] = None
    playback_date: datetime
    timestamp: Optional[datetime] = None

    @field_serializer('playback_date')
    def serialize_date(self, dt: datetime) -> str:
        return dt.strftime(LASTFM_DATETIME_FORMAT)

class ScrobbleCollectionTransfer(BaseModel):
    scrobbles: list[ScrobbleTransfer]