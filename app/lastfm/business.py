from app.lastfm.client import LastFMClient
from app.models.lastfm_models import Scrobble


class LastFMBusiness:
    def __init__(self, client: LastFMClient, username: str):
        self.client = client
        self.username = username

    def fetch_scrobbles(self, limit: int = None):
        raw_tracks = self.client.get_recent_tracks(self.username, limit=limit)

        return [
            Scrobble(
                track_id=str(track.playback_date),
                title=track.track.title,
                artist=track.track.artist.name,
                album=track.album if track.album else None,
                timestamp=str(track.playback_date),
            )
            for track in raw_tracks
        ]