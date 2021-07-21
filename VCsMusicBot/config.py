import os
from os import path
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "BACiG8IBUzHgsRmxIylKxDygVdOD0ZSCwKljGiA3KDVZjf--D6vU4TnEp2y0SIiJlDKxgPzslG_xfwzixeccwU8KQEqXqjAuAu3jz7pyEYTGpf16HfbGmy0BG1Q-BmgszhqIDjuoAdzQX4FO4QGhVYCBhQWdrK4--p8SPuq0uyNQ0IIMaw1aqkntfW1Pdxc9H03IulKVQQtpfP88WcPB4sAGCf_ig0zY8De4aaJ-cUG7EIGUl8EsRdFOBhl3YhIUEhMmF4P1JGngzODc0iFzeluUJhwKRvqY3_p8exLn8LuHpphZkVvcJaKGHxMDK_o8mofbKKkTww9KbFmiuyfIliLVZi0CqwA")
BOT_TOKEN = getenv("BOT_TOKEN"1757358349:AAG5bFstXXVaRFdFLrX6rPxQtuiYGxevpzQ")
BOT_NAME = getenv("BOT_NAME"Test Player RoBot")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "HiroshiBots")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/cf19dda907391656338eb.png")
admins = {}
API_ID = int(getenv("API_ID", "2155025"))
API_HASH = getenv("API_HASH","78c3c29a509ec1875789dd9c301ce106")
BOT_USERNAME = getenv("BOT_USERNAME")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "VCsMusicPlayer")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "zauteschat")
PROJECT_NAME = getenv("PROJECT_NAME", "VCsMusicBot")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/ZauteKm/VCsMusicBot")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "15"))
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
