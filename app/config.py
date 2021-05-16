import os
from . import app
from utils import MongoClient
from flask import render_template
from decouple import config as get_env
from flask_discord import DiscordOAuth2Session
from motor.motor_asyncio import AsyncIOMotorClient


os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

LOGIN_URL = "https://discord.com/api/oauth2/authorize?client_id=763626077292724264&redirect_uri=http%3A%2F%2F127.0.0.1%3A5000%2Fdiscord-login&response_type=code&scope=identify%20guilds"
BOT_INVITE = "https://discord.com/api/oauth2/authorize?client_id=763626077292724264&permissions=273115158&scope=bot%20applications.commands"
REDIRECT_URI = "http://127.0.0.1:5000/callback"

FLASK_SECRET_KEY = bytes(get_env("FLASK_SECRET_KEY"), encoding='utf8')
MONGO_URI = get_env("MONGO_SECRET")
CLI_SECRET = get_env("CLIENT_SECRET")
CLI_ID = int(get_env("CLIENT_ID"))
BOT_TOKEN = get_env("BOT_TOKEN")

app.secret_key = FLASK_SECRET_KEY
app.config["DISCORD_CLIENT_ID"] = CLI_ID
app.config["DISCORD_CLIENT_SECRET"] = CLI_SECRET
app.config["DISCORD_REDIRECT_URI"] = REDIRECT_URI
app.config["DISCORD_BOT_TOKEN"] = BOT_TOKEN

discord = DiscordOAuth2Session(app)
mongo = AsyncIOMotorClient(MONGO_URI)

def better_render(html_name, **kwargs):

    _user = None
    if discord.get_authorization_token():
        _user = discord.fetch_user()
    
    return render_template(html_name, user=_user, **kwargs)

class db(object):

    def __init__(self):
        
        self.guild_settings = MongoClient(mongo["Guild"], "Config")

        _botdb = mongo["BotData"]
        self.cmd_stats = MongoClient(_botdb, "CommandStats")
        self.bl = MongoClient(_botdb, "Blacklisted")

        _udb = mongo["User"]
        self.userconfig = MongoClient(_udb, "Config")
