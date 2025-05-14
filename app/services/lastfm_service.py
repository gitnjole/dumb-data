import pylast
import logging
from app.config import settings


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class LastFmService:
    """
    Service for fetching data from LastFM.
    """

    def __init__(self, network: pylast.LastFMNetwork):
        """
        network: an instance of pylast.LastFMNetwork containing authorised
        user data.

        You should obtain a preconfigured network object through a
        Depends(get_lastfm_network) method instead of creating an object
        of this class, unless you know what you're doing.
        """
        self.network = network


    def get_scrobbles(self, limit: int):
        user = self.network.get_user(settings.LASTFM_USERNAME)

        # Currently all business logic contained within this try block.
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