from flask import Blueprint, render_template
from app.models import Tour

user_bp = Blueprint('user', __name__)

@user_bp.route('/')
def index():
    tours = Tour.query.all()
    return render_template('index.html', tours=tours)
