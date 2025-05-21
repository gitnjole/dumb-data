from pydantic import BaseModel
from typing import Optional

class Scrobble(BaseModel):
    track_id: str
    track: str
    artist: str
    album: Optional[str] = None
    playback_date: str

class ScrobbleResponse(BaseModel):
    scrobbles: list[Scrobble]