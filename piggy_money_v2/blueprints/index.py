
from flask import Blueprint, request, session, redirect, url_for, \
     render_template



bp = Blueprint('piggy_money', __name__)

@bp.route("/")
def index():
    return "hallo~"