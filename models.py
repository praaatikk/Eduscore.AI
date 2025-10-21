from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

# ------------------------------
# User Table
# ------------------------------
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    predictions = db.relationship('Prediction', backref='user', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


# ------------------------------
# Prediction Table
# ------------------------------
class Prediction(db.Model):
    __tablename__ = 'predictions'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    gender = db.Column(db.String(10))
    race_ethnicity = db.Column(db.String(20))
    parental_level_of_education = db.Column(db.String(50))
    lunch = db.Column(db.String(20))
    test_preparation_course = db.Column(db.String(20))
    reading_score = db.Column(db.Float)
    writing_score = db.Column(db.Float)
    predicted_math_score = db.Column(db.Float)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
