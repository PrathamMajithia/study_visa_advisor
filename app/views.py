from flask import Blueprint, render_template, request
from .main import get_response

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('chat.html')

@bp.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    prompt = msg
    return get_response(prompt)