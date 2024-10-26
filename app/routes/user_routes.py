# app/routes/user_routes.py
from flask import Blueprint, request, jsonify
from app.models.user import User
from app import db

bp = Blueprint('users', __name__)

@bp.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    new_user = User(name=data['name'], badge_id=data['badge_id'], role=data.get('role', 'employee'))
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created successfully"}), 201

@bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{"id": user.id, "name": user.name, "badge_id": user.badge_id, "role": user.role} for user in users]), 200
