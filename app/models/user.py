# app/models/user.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

# Importation de 'db' après l'initialisation
from app import db

class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    badge_id = Column(String(50), unique=True, nullable=False)
    role = Column(String(50), default='employee')

    attendances = relationship('Attendance', backref='user', lazy=True)
