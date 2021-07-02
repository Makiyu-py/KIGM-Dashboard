from flask import render_template, redirect, url_for, abort
from flask_discord import Unauthorized
from .config import db, better_render
from . import app, discord


_mongo = db()  # main db instance

@app.route("/")
def homepage():
    return better_render("home.html", title="Home")

# arc.io widget
@app.route("/arc-sw.js")
def arc_js():
    return redirect("https://arc.io/arc-sw.js")

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
def dashboard():
    return abort(404)

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
