import json
import os

from flask import (Flask, make_response, redirect, render_template, request,
                   request_started, session, url_for, jsonify, abort)
from werkzeug.routing import BuildError
from functools import wraps


app = Flask(__name__)
app.secret_key = os.urandom(61)
app.session_cookie_name = "reyes"
app.apis = 2


def login_required(function):

    @wraps(function)
    def wrapper(*args, **kwargs):
        if "username" not in session:
            abort(401)
        return function(*args, **kwargs)
    return wrapper


@app.before_request
def before():
    pass


@app.errorhandler(BuildError)
def builderror(error):
    return "BuildError"


@app.route("/users")
@login_required
def users():
    with open("files.json", encoding="utf-8", mode="r") as fp:
        users = json.load(fp)
        return jsonify(users)


@app.errorhandler(404)
def _404(error):
    r = make_response(f"No encontrado {error}")
    r.headers["X-remain-request"] = 87
    return redirect(url_for("index"))


@app.route("/", methods=["GET"])
@login_required
def index():
    if session.get("username", False):
        return render_template("index.html", username=session['username'])
    else:
        return "can you login?"


@app.route("/login/<username>/", methods=["GET"])
def login(username):
    session["username"] = username
    return f'logueado {session["username"] } '


@app.route("/logout", methods=["GET"])
def logout():
    if "username" in session:
        del session["username"]
    return "deslogueado"


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=3200)
