from fastapi import APIRouter, Depends, Query
from typing import Optional
from app.lastfm.dependencies import get_lastfm_business
from app.lastfm.business import LastFMBusiness
from app.models.lastfm_models import ScrobbleCollectionTransfer

router = APIRouter()

@router.get("/scrobbles", response_model=ScrobbleCollectionTransfer)
async def get_scrobbles(
    limit: Optional[int] = Query(None),
    business: LastFMBusiness = Depends(get_lastfm_business)
):
    return business.fetch_scrobbles(limit=limit)