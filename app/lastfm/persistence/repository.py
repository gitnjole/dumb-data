from abc import ABC, abstractmethod
from app.models.lastfm_models import ScrobbleTransfer, ScrobbleCollectionTransfer

class ScrobbleRepositoryInterface(ABC):
    @abstractmethod
    def find_by_name(self, name: str) -> ScrobbleTransfer:
        pass

    @abstractmethod
    def find_all(self, limit: int = None) -> ScrobbleCollectionTransfer:
        pass

    @abstractmethod
    def find_by_recent_timestamp(self, timestamp: str) -> ScrobbleTransfer:
        pass

class ScrobbleWriterInterface(ABC):
    @abstractmethod
    def save(self, scrobble: ScrobbleTransfer) -> ScrobbleTransfer:
        pass

    @abstractmethod
    def save_collection(self, scrobbles: ScrobbleCollectionTransfer) -> None:
        pass