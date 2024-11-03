# app/models/attendance.py
from app import db

class Attendance(db.Model):
    __tablename__ = 'attendances'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=db.func.now())

    entry_time = db.Column(db.DateTime, nullable=True)
    exit_time = db.Column(db.DateTime, nullable=True)
    status = db.Column(db.String(20), nullable=False, default='Present') 
    event_type = db.Column(db.String(10), nullable=False)

    # user = db.relationship('User', backref=db.backref('attendances', lazy=True))
    user = db.relationship('User', back_populates='attendances')

