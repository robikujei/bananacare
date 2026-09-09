# auth.py
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_user, logout_user

from . import db
from .constants import ADMIN_ROLE, FARMER_ROLE, MAX_LENGTHS
from .forms import bounded_text, positive_number, text_field, text_fields
from .models import FarmerProfile, User

auth_bp = Blueprint("auth", __name__)

MIN_PASSWORD_LENGTH = 6


def _login(expected_role):
    """Handle the shared login flow while enforcing the selected portal role."""
    if current_user.is_authenticated:
        return redirect(url_for("main.dashboard"))

    if request.method == "POST":
        username = text_field("username")
        password = request.form.get("password", "")
        user = User.query.filter_by(username=username, role=expected_role).first()

        if user and user.check_password(password):
            login_user(user)
            flash("Welcome back!", "success")
            return redirect(url_for("main.dashboard"))

        flash("Invalid username, password, or account type.", "danger")

    return render_template("login.html", role=expected_role)


@auth_bp.route("/farmer/login", methods=["GET", "POST"])
def farmer_login():
    return _login(FARMER_ROLE)


@auth_bp.route("/admin/login", methods=["GET", "POST"])
def admin_login():
    return _login(ADMIN_ROLE)


@auth_bp.route("/farmer/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        fields = text_fields(
            "username",
            "password",
            "full_name",
            "contact_number",
            "location",
            "farm_size",
            "banana_variety",
        )
        if not all(fields.values()):
            flash("All required fields must be completed.", "danger")
            return render_template("register.html", data=fields)

        if len(fields["password"]) < MIN_PASSWORD_LENGTH:
            flash(
                f"Password must contain at least {MIN_PASSWORD_LENGTH} characters.",
                "danger",
            )
            return render_template("register.html", data=fields)

        # Validate cheap, in-memory constraints (length, numeric format)
        # before touching the database with a uniqueness lookup.
        try:
            username = bounded_text(fields["username"], "Username", MAX_LENGTHS["username"])
            full_name = bounded_text(
                fields["full_name"], "Full name", MAX_LENGTHS["full_name"]
            )
            contact_number = bounded_text(
                fields["contact_number"], "Contact number", MAX_LENGTHS["contact_number"]
            )
            location = bounded_text(fields["location"], "Location", MAX_LENGTHS["location"])
            banana_variety = bounded_text(
                fields["banana_variety"], "Banana variety", MAX_LENGTHS["banana_variety"]
            )
            farm_size = positive_number(fields["farm_size"])
        except ValueError as exc:
            flash(str(exc), "danger")
            return render_template("register.html", data=fields)

        if User.query.filter_by(username=username).first():
            flash("That username is already in use.", "danger")
            return render_template("register.html", data=fields)

        user = User(username=username, role=FARMER_ROLE)
        user.set_password(fields["password"])
        user.profile = FarmerProfile(
            full_name=full_name,
            contact_number=contact_number,
            location=location,
            farm_size=farm_size,
            banana_variety=banana_variety,
        )
        db.session.add(user)
        db.session.commit()
        flash("Registration complete. You may now sign in.", "success")
        return redirect(url_for("auth.farmer_login"))

    return render_template("register.html", data={})


@auth_bp.route("/logout")
def logout():
    logout_user()
    flash("You have been signed out.", "info")
    return redirect(url_for("main.index"))