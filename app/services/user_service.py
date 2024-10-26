from app.models.user import User
from app import db

def create_user(name, badge_id, role='employee'):
    user = User(name=name, badge_id=badge_id, role=role)
    db.session.add(user)
    db.session.commit()
    return user

def get_user_by_badge(badge_id):
    return User.query.filter_by(badge_id=badge_id).first()
