from pydantic import BaseModel
from typing import Optional

class ScrobbleTransfer(BaseModel):
    track: str
    artist: str
    album: Optional[str] = None
    playback_date: str

class ScrobbleCollectionTransfer(BaseModel):
    scrobbles: list[ScrobbleTransfer]