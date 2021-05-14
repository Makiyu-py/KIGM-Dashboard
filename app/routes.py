from flask import render_template, redirect, url_for
from .config import db
from . import app


_mongo = db()  # main db instance

@app.route("/")
def homepage():
    return render_template("home.html", title="Home")

@app.route("/support")
def support():
    return redirect("https://discord.gg/jz4WxkB")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', title="404")

# TODO
#    - Actual Dashboard (via flask-discord)
#    - Add login page from the "login with discord" btn
#    - Getting cmds then outputting it to a page
#      (I don't have ideas on how to do that yet)

