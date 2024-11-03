
from flask import Blueprint, request, jsonify
from app.models.user import User
from app import db

bp = Blueprint('users', __name__)

@bp.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    
    # Validation de la présence des champs requis
    required_fields = ['name', 'badge_id', 'email', 'phone', 'department']
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        return jsonify({"error": f"Missing fields: {', '.join(missing_fields)}"}), 400
    
    new_user = User(
        name=data['name'],
        badge_id=data['badge_id'],
        role=data.get('role', 'employee'),
        email=data['email'],
        phone=data['phone'],
        department=data['department']
    )
    
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created successfully"}), 201

@bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([
        {
            "id": user.id,
            "name": user.name,
            "badge_id": user.badge_id,
            "role": user.role,
            "email": user.email,
            "phone": user.phone,
            "department": user.department
        }
        for user in users
    ]), 200
