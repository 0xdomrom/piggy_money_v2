
from flask import Blueprint, request, session, redirect, url_for, \
     render_template, render_template_string, jsonify

from piggy_money_v2.dbmodel import Users, Accounts, Session, Transactions

import os

bp = Blueprint('piggy_money', __name__)

@bp.after_request
def add_header(r):
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers["Cache-control"] = "public, max-age=0"
    return r


@bp.route("/")
def index():
    with open("./piggy_money_v2/templates/index.html") as f:
        template = f.read()
    return render_template_string(template)
    #return render_template('index.html')

@bp.route("/api/test")
def api_test():
    return "Test~"

@bp.route("/api/authenticate/", methods=["POST"])
def api_authenticate():
    print(request)
    print(request.username)
    print(request.password)
    dbsession = Session()
    dbsession.query(Users).filter(Users.username.has())
    return jsonify({"valid":True,"token":"abcdef1234567890"})
