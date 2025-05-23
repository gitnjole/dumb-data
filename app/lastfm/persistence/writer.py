from datetime import datetime
from app.lastfm.models.sql_models import ScrobbleORM
from app.models.lastfm_models import ScrobbleTransfer, ScrobbleCollectionTransfer, ScrobbleResponseTransfer
from .repository import ScrobbleWriterInterface
from sqlalchemy.orm import Session

class ScrobbleWriter(ScrobbleWriterInterface):
    def __init__(self, db: Session):
        self.db = db

    def save(self, scrobble: ScrobbleTransfer) -> ScrobbleResponseTransfer:
        db_obj = self._insert_timestamp_scrobble(scrobble)

        try:
            self.db.add(db_obj)
            self.db.commit()
            self.db.refresh(db_obj)
            return ScrobbleResponseTransfer(is_successful=True)
        except Exception as e:
            self.db.rollback()
            return ScrobbleResponseTransfer(
                is_successful=False,
                message=str(e)
            )
    
    def save_collection(self, scrobbles: ScrobbleCollectionTransfer) -> ScrobbleResponseTransfer:
        db_objects = self._insert_timestamp_collection(scrobbles)

        try:
            self.db.add_all(db_objects)
            self.db.commit()
            return ScrobbleResponseTransfer(
                is_successful=True
            )
        except Exception as e:
            self.db.rollback()
            return ScrobbleResponseTransfer(
                is_successful=False,
                message=str(e)
            )
        
    def _insert_timestamp_scrobble(self, scrobble: ScrobbleTransfer) -> ScrobbleORM:
        return scrobble.insert_timestamp()
        
    def _insert_timestamp_collection(self, collection: ScrobbleCollectionTransfer) -> list[ScrobbleORM]:
        ts = datetime.now()
        return [s.insert_timestamp() for s in collection.scrobbles]