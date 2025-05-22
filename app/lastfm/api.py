from fastapi import APIRouter, Depends, Query
from typing import Optional
import pylast

from app.lastfm.dependencies import get_lastfm_network
from app.lastfm.client import LastFMClient
from app.lastfm.business import LastFMBusiness
from app.models.lastfm_models import ScrobbleCollectionTransfer

router = APIRouter()

@router.get("/scrobbles", response_model=ScrobbleCollectionTransfer)
async def get_scrobbles(
    limit: Optional[int] = Query(None),
    network: pylast.LastFMNetwork = Depends(get_lastfm_network)
):
    client = LastFMClient(network)
    business = LastFMBusiness(client=client, username=network.username)
    return business.fetch_scrobbles(limit=limit)