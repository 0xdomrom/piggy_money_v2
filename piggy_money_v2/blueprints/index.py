
from flask import Blueprint, request, session, redirect, url_for, \
     render_template



bp = Blueprint('piggy_money', __name__)

@bp.route("/")
def index():
    return render_template('index.html')

@bp.route("/api/test")
def api_test():
    return "Test~"
