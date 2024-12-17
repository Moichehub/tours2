from app import db
from flask_login import UserMixin
import json

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

class Tour(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price_per_person = db.Column(db.Float, nullable=False)
    available_dates = db.Column(db.String(300))  # JSON-формат дати
    image = db.Column(db.String(300), nullable=True)

    def get_dates(self):
        return json.loads(self.available_dates)

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    tour_id = db.Column(db.Integer, db.ForeignKey('tour.id'), nullable=False)
    date = db.Column(db.String(100), nullable=False)
    people = db.Column(db.Integer, nullable=False)
    total_price = db.Column(db.Float, nullable=False)
