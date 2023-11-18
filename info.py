import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'Media_Search')
API_ID = 10247139
API_HASH = "96b46175824223a33737657ab943fd6a"
BOT_TOKEN = "6559513905:AAGpz_JC8WUZlQCbbGilS1qCQwnBbF6u8hQ"

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))

# Admins, Channels & Users
ADMINS = [5894098166]
CHANNELS = [-1001813199018]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', "").split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = "-1001967738594"
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else auth_channel
AUTH_GROUPS = [int(admin) for admin in environ.get("AUTH_GROUPS", "").split()]

# MongoDB information
DATABASE_URI = 'mongodb+srv://480p:encode@cluster0.7fgwrif.mongodb.net/?retryWrites=true&w=majority'
DATABASE_NAME = 'terabhai'
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'libory')

# Messages
default_start_msg = """
**Hi**
Here you can search files in Inline mode as well as PM, Use the below buttons to search files or send me the name of Anime to search, Unable to see full filename , no problem just turn your phone in horizontal direction
"""
START_MSG = environ.get('START_MSG', default_start_msg)

FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "")
OMDB_API_KEY = environ.get("OMDB_API_KEY", "http://www.omdbapi.com/?i=tt3896198&apikey=67f23fef")
if FILE_CAPTION.strip() == "":
    CUSTOM_FILE_CAPTION=None
else:
    CUSTOM_FILE_CAPTION=FILE_CAPTION
if OMDB_API_KEY.strip() == "":
    API_KEY=None
else:
    API_KEY=OMDB_API_KEY
