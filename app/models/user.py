from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app import db

class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    badge_id = Column(String(50), unique=True, nullable=False)
    role = Column(String(50), default='employee')
    email = Column(String(100), nullable=False)
    phone = Column(String(100), nullable=False)
    department = Column(String(100), nullable=False)

    attendances = db.relationship('Attendance', back_populates='user', lazy=True)
