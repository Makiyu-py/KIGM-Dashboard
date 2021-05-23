from flask import render_template, redirect, url_for, abort
from .config import BOT_TOKEN, db, better_render
from utils.discord_stuff import get_mutuals
from flask_discord import Unauthorized
from . import app, discord


_mongo = db()  # main db instance

@app.route("/")
def homepage():
    return better_render("home.html", title="Home")

@app.route("/login")
def login():
    return discord.create_session(scope=['identify', 'guilds'])

@app.route("/callback/")
def callback():
    discord.callback()
    return redirect(url_for("homepage"))

@app.route("/commands")
def cmd_infos():
    return abort(404)

@app.route("/dashboard")
async def dashboard():
    user_guilds = discord.fetch_guilds()
    mutuals = await get_mutuals(user_guilds, token=BOT_TOKEN)

    return better_render("dashboard.html", title="Dashboard", guilds=mutuals)

@app.route("/support")
def support():
    return redirect("https://discord.gg/jz4WxkB")

@app.errorhandler(404)
def page_not_found(e):
    return better_render('404.html', title="404")

@app.errorhandler(Unauthorized)
def page_not_found(e):
    return redirect(url_for("login"))

# TODO
#    - Actual Dashboard (via flask-discord)
#    - Getting cmds then outputting it to a page
#      (I don't have ideas on how to do that yet)
