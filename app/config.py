from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    API_KEY = os.getenv('API_KEY')
    API_SECRET = os.getenv('API_SECRET')
    LASTFM_USERNAME = os.getenv('LASTFM_USERNAME')
    LASTFM_PASSWORD = os.getenv('LASTFM_PASSWORD')

    @property
    def LASTFM_HASHED_PASSWORD(self):
        import pylast
        return pylast.md5(self.LASTFM_PASSWORD)

settings = Settings()