import pylast
from fastapi import Depends
from sqlalchemy.orm import Session
from app.core.config import settings
from app.core.database import get_db
from app.lastfm.client import LastFMClient
from app.lastfm.business import LastFMBusiness

class LastFmNetworkManager:
    def __init__(self):
        self.network = None

    def authenticate(self):
        self.network = pylast.LastFMNetwork(
            api_key=settings.API_KEY,
            api_secret=settings.API_SECRET,
            username=settings.LASTFM_USERNAME,
            password_hash=settings.LASTFM_HASHED_PASSWORD,
        )

        try:
            self.network.get_user(settings.LASTFM_USERNAME).get_name()
        except pylast.WSError as e:
            raise Exception(f"Authentication failed: {str(e)}")

    def get_network(self):
        if not self.network:
            self.authenticate()
        return self.network

_lastfm_manager = LastFmNetworkManager()

async def get_lastfm_network():
    """
    Dependency injection for FastAPI routes.
    Returns an authenticated LastFM network.
    """
    return _lastfm_manager.get_network()

def get_lastfm_business(
        network: pylast.LastFMNetwork = Depends(get_lastfm_network),
        db: Session = Depends(get_db)
) -> LastFMBusiness:
    client = LastFMClient(network)
    return LastFMBusiness(client=client, username=network.username, db=db)