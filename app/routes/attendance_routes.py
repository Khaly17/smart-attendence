# app/routes/attendance_routes.py
from flask import Blueprint, request, jsonify
from app.models.attendance import Attendance
from app.models.user import User
from app import db
from datetime import datetime


bp = Blueprint('attendances', __name__)

@bp.route('/attendances', methods=['POST'])
def log_attendance():
    data = request.get_json()
    user = User.query.filter_by(badge_id=data['badge_id']).first()

    if not user:
        return jsonify({"error": "User not found"}), 404

    # Determine if it's an entry or exit event
    event_type = data.get('event_type')  # 'entry' or 'exit'

    if event_type == 'entry':
        new_attendance = Attendance(user_id=user.id, entry_time=datetime.now(), status="Present", event_type="entry")
    elif event_type == 'exit':
        # Get the latest attendance entry for this user to update exit time
        new_attendance = Attendance.query.filter_by(user_id=user.id, event_type="entry").order_by(Attendance.entry_time.desc()).first()
        if new_attendance and new_attendance.exit_time is None:
            new_attendance.exit_time = datetime.now()
            new_attendance.event_type = "exit"
            db.session.commit()
            return jsonify({"message": "Exit time recorded"}), 200
        else:
            return jsonify({"error": "No matching entry record found"}), 400
    else:
        return jsonify({"error": "Invalid event type"}), 400

    # Save the entry event
    db.session.add(new_attendance)
    db.session.commit()

    return jsonify({"message": f"{event_type.capitalize()} time logged"}), 201

@bp.route('/attendances', methods=['GET'])
def get_attendances():
    # Optional filtering by user_id
    user_id = request.args.get('user_id', type=int)
    if user_id:
        attendances = Attendance.query.filter_by(user_id=user_id).all()
    else:
        attendances = Attendance.query.all()

    attendance_list = []
    for attendance in attendances:
        attendance_list.append({
            "id": attendance.id,
            "user_id": attendance.user_id,
            "timestamp": attendance.timestamp,
            "status": attendance.status,
            "entry_time": attendance.entry_time,
            "exit_time": attendance.exit_time  
        })

    return jsonify(attendance_list), 200