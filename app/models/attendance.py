# app/models/attendance.py
from app import db

class Attendance(db.Model):
    __tablename__ = 'attendances'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=db.func.now())


    user = db.relationship('User', backref=db.backref('attendances', lazy=True))
