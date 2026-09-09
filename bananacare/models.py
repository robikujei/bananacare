# models.py — unchanged (no schema edits made, as instructed)
from datetime import UTC, date, datetime

from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from . import db
from .constants import ASSISTANCE_STATUSES, FARMER_ROLE, REPORT_STATUSES


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(10), nullable=False, default=FARMER_ROLE)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(UTC), nullable=False)
    profile = db.relationship(
        "FarmerProfile",
        backref="user",
        uselist=False,
        cascade="all, delete-orphan",
    )

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class FarmerProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), unique=True, nullable=False)
    full_name = db.Column(db.String(100), nullable=False)
    contact_number = db.Column(db.String(20), nullable=False)
    location = db.Column(db.String(150), nullable=False)
    farm_size = db.Column(db.Numeric(10, 2), nullable=False)
    banana_variety = db.Column(db.String(80), nullable=False)
    planting_date = db.Column(db.Date, nullable=True)
    estimated_production = db.Column(db.Numeric(10, 2), nullable=True)
    reports = db.relationship(
        "DiseaseReport", backref="farmer", cascade="all, delete-orphan"
    )
    assistance_requests = db.relationship(
        "Assistance", backref="farmer", cascade="all, delete-orphan"
    )


class DiseaseReport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    farmer_id = db.Column(db.Integer, db.ForeignKey("farmer_profile.id"), nullable=False)
    date_reported = db.Column(db.Date, default=date.today, nullable=False)
    problem_type = db.Column(db.String(60), nullable=False)
    affected_area = db.Column(db.Numeric(10, 2), nullable=False)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(30), default=REPORT_STATUSES[0], nullable=False)
    remarks = db.Column(db.Text, default="")


class Assistance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    farmer_id = db.Column(db.Integer, db.ForeignKey("farmer_profile.id"), nullable=False)
    assistance_type = db.Column(db.String(80), nullable=False)
    date_requested = db.Column(db.Date, default=date.today, nullable=False)
    date_provided = db.Column(db.Date, nullable=True)
    status = db.Column(db.String(30), default=ASSISTANCE_STATUSES[0], nullable=False)
    recommendation = db.Column(db.Text, default="")