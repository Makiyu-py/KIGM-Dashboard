from utils import MongoClient
from decouple import config as get_env
from motor.motor_asyncio import AsyncIOMotorClient


LOGIN_URL = "https://discord.com/api/oauth2/authorize?client_id=763626077292724264&redirect_uri=http%3A%2F%2F127.0.0.1%3A5000%2Fdiscord-login&response_type=code&scope=identify%20guilds"
BOT_INVITE = "https://discord.com/api/oauth2/authorize?client_id=763626077292724264&permissions=273115158&scope=bot%20applications.commands"
REDIRECT_URI = "http://127.0.0.1:5000/callback"

MONGO_URI = get_env("MONGO_SECRET")
CLI_SECRET = get_env("CLIENT_SECRET")
CLI_ID = int(get_env("CLIENT_ID"))
BOT_TOKEN = get_env("BOT_TOKEN")

mongo = AsyncIOMotorClient(MONGO_URI)

class db(object):

    def __init__(self):
        
        self.guild_settings = MongoClient(mongo["Guild"], "Config")

        _botdb = mongo["BotData"]
        self.cmd_stats = MongoClient(_botdb, "CommandStats")
        self.bl = MongoClient(_botdb, "Blacklisted")

        _udb = mongo["User"]
        self.userconfig = MongoClient(_udb, "Config")
