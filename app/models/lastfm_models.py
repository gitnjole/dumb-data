from pydantic import BaseModel
from typing import Optional

class Scrobble(BaseModel):
    track_id: str
    title: str
    artist: str
    album: Optional[str] = None
    timestamp: str

class ScrobbleResponse(BaseModel):
    scrobbles: list[Scrobble]