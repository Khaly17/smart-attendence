# app/routes/attendance_routes.py
from flask import Blueprint, request, jsonify
from app.models.attendance import Attendance
from app.models.user import User
from app import db

bp = Blueprint('attendances', __name__)

@bp.route('/attendances', methods=['POST'])
def log_attendance():
    data = request.get_json()
    user = User.query.filter_by(badge_id=data['badge_id']).first()
    if user:
        new_attendance = Attendance(user_id=user.id)
        db.session.add(new_attendance)
        db.session.commit()
        return jsonify({"message": "Attendance logged"}), 201
    return jsonify({"error": "User not found"}), 404
