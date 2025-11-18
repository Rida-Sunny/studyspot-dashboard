# models.py
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()

# -----------------------------
# User Model
# -----------------------------
class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(50), nullable=False)  # e.g., student, admin
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<User {self.email}>"

# -----------------------------
# StudySpot Model
# -----------------------------
class StudySpot(db.Model):
    __tablename__ = "study_spots"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)  # Spot name
    location = db.Column(db.String(150), nullable=False)  # e.g., Library
    seating = db.Column(db.String(100))  # e.g., Tables, Couches
    noise_level = db.Column(db.String(50))  # e.g., Quiet, Moderate, Loud
    hours = db.Column(db.String(50))  # e.g., "8am-10pm"
    wifi_quality = db.Column(db.String(50))  # e.g., Strong, Weak
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<StudySpot {self.name} at {self.location}>"