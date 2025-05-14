import pylast

class LastFMClient:
    def __init__(self, network: pylast.LastFMNetwork):
        """
        network: an instance of pylast.LastFMNetwork containing authorised
        user data.

        You should obtain a preconfigured network object through a
        Depends(get_lastfm_network) method instead of creating an object
        of this class, unless you know what you're doing.
        """
        self.network = network

    def get_recent_tracks(self, username: str, limit: int = None):
        user = self.network.get_user(username)

        return user.get_recent_tracks(limit=limit)