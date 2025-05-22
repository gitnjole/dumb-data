from app.core.database import SessionLocal
from app.lastfm.models.sql_models import ScrobbleORM
from app.models.lastfm_models import ScrobbleTransfer, ScrobbleCollectionTransfer
from .repository import ScrobbleWriterInterface

class ScrobbleWriter(ScrobbleWriterInterface):
    def __init__(self):
        self.db = SessionLocal()

    def save(self, scrobble: ScrobbleTransfer) -> ScrobbleCollectionTransfer:
        db_obj = ScrobbleORM(**scrobble.model_dump())

        try:
            self.db.add(db_obj)
            self.db.commit()
            self.db.refresh(db_obj)
            return ScrobbleCollectionTransfer.model_validate(db_obj.__dict__)
        except Exception as e:
            self.db.rollback()
            raise
    
    def save_collection(self, scrobbles: ScrobbleCollectionTransfer) -> None:
        db_objects = [ScrobbleORM(**s.model_dump()) for s in scrobbles.scrobbles]

        try:
            self.db.add_all(db_objects)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise