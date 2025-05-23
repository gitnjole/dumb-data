from app.lastfm.client import LastFMClient
from app.models.lastfm_models import ScrobbleTransfer, ScrobbleCollectionTransfer
from app.lastfm.persistence.writer import ScrobbleWriter
from app.lastfm.persistence.reader import ScrobbleReader
from app.core.datetime_utils import parse_playback_date
from sqlalchemy.orm import Session

class LastFMBusiness:
    def __init__(self, client: LastFMClient, username: str, db: Session):
        self.client = client
        self.username = username
        self.writer = ScrobbleWriter(db)
        self.reader = ScrobbleReader(db)

    def fetch_scrobbles(self, limit: int = None)-> ScrobbleCollectionTransfer:
        raw_tracks = self.client.get_recent_tracks(self.username, limit=limit)

        collection = ScrobbleCollectionTransfer(
            scrobbles = [
                ScrobbleTransfer(
                    track=played.track.title,
                    artist=played.track.artist.name,
                    album=played.album if played.album else None,
                    playback_date=parse_playback_date(played.playback_date),
                )
                for played in raw_tracks
            ]
        )

        self._persist_scrobbles(collection)

        return collection
    
    def _persist_scrobbles(self, scrobbles: ScrobbleCollectionTransfer):
        self.writer.save_collection(scrobbles)
