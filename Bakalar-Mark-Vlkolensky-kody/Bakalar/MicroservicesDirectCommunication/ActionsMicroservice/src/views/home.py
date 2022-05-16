from quart import Blueprint, render_template


home = Blueprint("home", __name__)

@home.route("/")
async def welcome_page():
    return await render_template("home.html")
