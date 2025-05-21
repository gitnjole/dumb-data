from app.core.database import SessionLocal
from app.lastfm.models.sql_models import ScrobbleORM
from app.models.lastfm_models import Scrobble

class LastFMPersistence:
    def __init__(self):
        self.db = SessionLocal()

    def save_scrobble(self, scrobble: Scrobble):
        try:
            db_obj = ScrobbleORM(**scrobble.model_dump())
            self.db.add(db_obj)
            self.db.commit()
            self.db.refresh(db_obj)
            return db_obj
        except Exception as e:
            print(f"Error saving scrobble: {e}")
            self.db.rollback()
            raise
    
    def list_scrobbles(self):
        return self.db.query(ScrobbleORM).all()
