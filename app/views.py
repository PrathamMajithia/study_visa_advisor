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
    try:
        response = get_response(prompt)
    except Exception as e:
        response = "I'm sorry, I can't respond at the moment. Please try again later."
    return response
