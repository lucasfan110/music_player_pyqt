import logging

from PyQt6.QtGui import QColor


SEARCH_LIMIT = 15

LOGGING_LEVEL = logging.DEBUG
FORMAT = "[%(filename)s] %(funcName)s(), line %(lineno)s(%(levelname)s): %(message)s"

DOWNLOAD_AUDIO_TO = "downloads"
DOWNLOADS_PLAYLIST = DOWNLOAD_AUDIO_TO

PLAYLIST_DIRECTORY = "./playlists/"
DOWNLOADS_DIRECTORY = "./downloads/"

YOUTUBE_PREFIX = "https://www.youtube.com/watch?v="

THUMBNAIL_FOLDER = "thumbnails/"
SETTINGS_FILE = "settings.json"

CURRENT_PLAYING_SONG_COLOR = QColor(0, 150, 0)
