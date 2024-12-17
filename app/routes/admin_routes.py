from flask import Blueprint, jsonify, request
from app.models import Tour, db
from flask_login import login_required, current_user

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/tours', methods=['POST'])
@login_required
def create_tour():
    if not current_user.is_admin:
        return jsonify({'status': 'error', 'message': 'Доступ заборонено'}), 403

    data = request.json
    tour = Tour(
        title=data['title'],
        description=data['description'],
        price_per_person=data['price'],
        available_dates=json.dumps(data['dates']),
        image=data['image']
    )
    db.session.add(tour)
    db.session.commit()

    return jsonify({'status': 'success', 'message': 'Тур створено'})
