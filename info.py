import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = 10247139
API_HASH = "96b46175824223a33737657ab943fd6a"
BOT_TOKEN = "6047442812:AAH4J2NbWRLRhgCbAwFuSrBbpBC1vPsasFs"

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))

# Admins, Channels & Users
ADMINS = [5894098166]
CHANNELS = [-1002100546607]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', "").split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = "-1001159872623"
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else auth_channel
AUTH_GROUPS = [int(admin) for admin in environ.get("AUTH_GROUPS", "").split()]

# MongoDB information
DATABASE_URI = 'mongodb+srv://480p:encode@cluster0.7fgwrif.mongodb.net/?retryWrites=true&w=majority'
DATABASE_NAME = 'filesharexbot'
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Messages
default_start_msg = """
**Hi, I'm Somayuki**
Here you can search files in Inline mode as well as PM, Use the below buttons to search files or send me the name of file to search.
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
