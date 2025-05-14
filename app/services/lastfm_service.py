import pylast
import logging
from app.config import settings


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class LastFmService:
    def __init__(self, network: pylast.LastFMNetwork):
        self.network = network

    def get_scrobbles(self, limit: int):
        user = self.network.get_user(settings.LASTFM_USERNAME)
        try:
            scrobbles = user.get_recent_tracks(limit=limit)
            if not scrobbles:
                logger.warning(f"No scrobbles found for {user}")

            result = []
            for track in scrobbles:
                track_data = {
                    "track_id": str(track.playback_date),
                    "title": track.track.title,
                    "artist": track.track.artist.name,
                    "timestamp": str(track.playback_date),
                }

                if track.album:
                    track_data["album"] = track.album
                else:
                    track_data["album"] = None

                result.append(track_data)
            return result
        except pylast.WSError as e:
            raise Exception(f"Error fetching tracks: {str(e)}")