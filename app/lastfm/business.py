from app.lastfm.client import LastFMClient
from app.models.lastfm_models import ScrobbleTransfer


class LastFMBusiness:
    def __init__(self, client: LastFMClient, username: str):
        self.client = client
        self.username = username

    def fetch_scrobbles(self, limit: int = None)-> ScrobbleTransfer:
        raw_tracks = self.client.get_recent_tracks(self.username, limit=limit)

        return [
            ScrobbleTransfer(
                track=played.track.title,
                artist=played.track.artist.name,
                album=played.album if played.album else None,
                playback_date=played.playback_date,
            )
            for played in raw_tracks
        ]