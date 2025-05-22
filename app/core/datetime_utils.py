from datetime import datetime

LASTFM_DATETIME_FORMAT = "%d %B %Y, %H:%M"

def parse_playback_date(raw: str) -> datetime:
    return datetime.strptime(raw, LASTFM_DATETIME_FORMAT)
