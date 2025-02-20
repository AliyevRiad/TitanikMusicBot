import re
import random
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "22457156"))
API_HASH = getenv("API_HASH", "6787a66c5c7d4018a01fe4d5d7249992")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "7186753157:AAGacxd_mlmehLrfDHotzV2q-Kgk3LIaQyI-WhM")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://ForzaMusicBot:ForzaMusicBot@forzamusicbot.z9u2c.mongodb.net/?retryWrites=true&w=majority")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 180))

# Chat id of a group for logging bot's activities
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1002345181976"))

# Get this value from @MissRose_Bot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "6305761724"))

# Fill Queue Limit . Example - 15
QUEUE_LIMIT = int(getenv("QUEUE_LIMIT", "20"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)

UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/SohbetFc")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/ForzaBoots/")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", None))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 104857600))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from Replit
STRING1 = getenv("STRING_SESSION", "AgFWq0QAFiM7ndKPIqJfLxyLGYj8H-nMJyu4qztVQ4t68i4YTGVEzpocnNRGSOnncO2VQzujmErBeIJNYuO7KrgC5F1nVymbvlGnPE6UYi0WJPpP_xexFU2ekh4t2PWiD5luOAkljWQstVz4qpr2p4AZgsWI1hunZnR8daC2FPq6vGTFUNmHHzpUhPeOjqYXqa6M06GMRhNE4Yd35q6QPJx2JiLMrqeG7JVMjkBc09ufMwa1MEZPr6t-O9_QMeIC42IARUNCfEzKfeBzEeEuAzjGYOiXMG9CLyZt15_1hKtvBZEfDSo2KHw9emjbrfyI6ODs_vPco0J_KiTL1tj-MBBQE5Dp0gAAAAGurfq1AA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = ["https://files.catbox.moe/h2bep4.jpg"]
PING_IMG_URL = ["https://files.catbox.moe/h2bep4.jpg"]
STATS_IMG_URL = ["https://files.catbox.moe/h2bep4.jpg"]
PLAYLIST_IMG_URL = getenv(
    "PLAYLIST_IMG_URL", "https://files.catbox.moe/h2bep4.jpg"
)
TELEGRAM_AUDIO_URL = getenv(
    "TELEGRAM_AUDIO_URL", "https://files.catbox.moe/h2bep4.jpg"
)
TELEGRAM_VIDEO_URL = getenv(
    "TELEGRAM_VIDEO_URL", "https://files.catbox.moe/h2bep4.jpg"
)
STREAM_IMG_URL = getenv(
    "STREAM_IMG_URL", "https://files.catbox.moe/h2bep4.jpg"
)
SOUNCLOUD_IMG_URL = getenv(
    "SOUNCLOUD_IMG_URL", "https://files.catbox.moe/h2bep4.jpg"
)
YOUTUBE_IMG_URL = getenv(
    "YOUTUBE_IMG_URL", "https://files.catbox.moe/h2bep4.jpg"
)
SPOTIFY_ARTIST_IMG_URL = getenv(
    "SPOTIFY_ARTIST_IMG_URL", "https://files.catbox.moe/h2bep4.jpg"
)
SPOTIFY_ALBUM_IMG_URL = getenv(
    "SPOTIFY_ALBUM_IMG_URL", "https://files.catbox.moe/h2bep4.jpg"
)
SPOTIFY_PLAYLIST_IMG_URL = getenv(
    "SPOTIFY_PLAYLIST_IMG_URL", "https://files.catbox.moe/h2bep4.jpg"
)


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
