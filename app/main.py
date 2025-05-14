import pylast
import tempfile

from fastapi import FastAPI, Depends, Query
from typing import Optional

from app.dependencies import get_lastfm_network
from app.models.lastfm_models import ScrobbleResponse
from app.services.lastfm_service import LastFmService


app = FastAPI()
TEMP_DIR = tempfile.mkdtemp()

@app.get("/")
async def health_check():
    return {"status": "ok"}

@app.get("/scrobbles", response_model=ScrobbleResponse)
async def get_scrobbles(
    limit: Optional[int] = Query(None),
    network: pylast.LastFMNetwork = Depends(get_lastfm_network)
):
    lastfm_service = LastFmService(network)
    scrobbles = lastfm_service.get_scrobbles(limit=limit)
    return {"scrobbles": scrobbles}
