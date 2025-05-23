from datetime import datetime
from app.lastfm.models.sql_models import ScrobbleORM
from app.models.lastfm_models import ScrobbleTransfer, ScrobbleCollectionTransfer
from .repository import ScrobbleWriterInterface
from sqlalchemy.orm import Session

class ScrobbleWriter(ScrobbleWriterInterface):
    def __init__(self, db: Session):
        self.db = db

    def save(self, scrobble: ScrobbleTransfer) -> ScrobbleCollectionTransfer:
        scrobble_prepared = self._insert_timestamp_scrobble(scrobble)
        db_obj = ScrobbleORM(**scrobble_prepared)

        try:
            self.db.add(db_obj)
            self.db.commit()
            self.db.refresh(db_obj)
            return ScrobbleCollectionTransfer.model_validate(db_obj.__dict__)
        except Exception as e:
            self.db.rollback()
            raise
    
    def save_collection(self, scrobbles: ScrobbleCollectionTransfer) -> None:
        collection_prepared = self._insert_timestamp_collection(scrobbles)
        db_objects = [ScrobbleORM(**s) for s in collection_prepared]

        try:
            self.db.add_all(db_objects)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise
        
    def _insert_timestamp_scrobble(self, scrobble: ScrobbleTransfer) -> dict:
        return {**scrobble.model_dump(), 'timestamp': datetime.now()}
    
    def _insert_timestamp_collection(self, collection: ScrobbleCollectionTransfer) -> list[dict]:
        timestamp = datetime.now()
        return [{**s.model_dump(), 'timestamp': timestamp} for s in collection.scrobbles]