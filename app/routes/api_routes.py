from flask import Blueprint, jsonify, request, render_template
from app.models import Tour, Booking, db
from flask_login import login_required, current_user
import json

api_bp = Blueprint('api', __name__)

# Отримати всі тури (для пошуку)
@api_bp.route('/tours', methods=['GET'])
def get_tours():
    search = request.args.get('search', '')
    tours = Tour.query.filter(Tour.title.contains(search)).all()
    return render_template('components/tour_card.html', tours=tours)

# Отримати форму бронювання
@api_bp.route('/book/<int:tour_id>', methods=['GET'])
def get_booking_form(tour_id):
    tour = Tour.query.get(tour_id)
    return render_template('components/booking_form.html', tour=tour)

# Здійснити бронювання
@api_bp.route('/book', methods=['POST'])
@login_required
def create_booking():
    data = request.form
    tour_id = int(data['tour_id'])
    date = data['date']
    people = int(data['people'])

    tour = Tour.query.get(tour_id)
    total_price = tour.price_per_person * people

    booking = Booking(user_id=current_user.id, tour_id=tour_id, date=date, people=people, total_price=total_price)
    db.session.add(booking)
    db.session.commit()

    return jsonify({'status': 'success', 'message': 'Бронювання створено', 'total_price': total_price})
