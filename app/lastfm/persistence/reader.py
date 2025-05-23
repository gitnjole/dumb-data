from app.lastfm.models.sql_models import ScrobbleORM
from app.models.lastfm_models import ScrobbleTransfer, ScrobbleCollectionTransfer
from .repository import ScrobbleRepositoryInterface
from sqlalchemy.orm import Session

class ScrobbleReader(ScrobbleRepositoryInterface):
    def __init__(self, db: Session):
        self.db = db

    def find_by_name(self, name: str) -> ScrobbleTransfer:
        result = self.db.query(ScrobbleORM).filter(ScrobbleORM.track == name).all()
        if not result:
            return None
        return self._extract_to_transfer(result)

    def find_all(self, limit: int = None) -> ScrobbleCollectionTransfer:
        query = self.db.query(ScrobbleORM)
        if limit:
            query = query.limit(limit)
        results = query.all()

        return ScrobbleCollectionTransfer(
            scrobbles=[self._extract_to_transfer(r) for r in results]
        )

    def find_by_recent_timestamp(self, timestamp) -> ScrobbleTransfer:
        result = self.db.query(ScrobbleORM).filter(
            ScrobbleORM.timestamp == timestamp
            ).first()
        if not result:
            return None

        return self._extract_to_transfer(result)

    def _extract_to_transfer(self, orm_obj: ScrobbleORM) -> ScrobbleTransfer:
        return ScrobbleTransfer(
            track=orm_obj.track,
            artist=orm_obj.artist,
            album=orm_obj.album,
            playback_date=orm_obj.playback_date,
        )