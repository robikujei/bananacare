from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_user, logout_user

from . import db
from .constants import ADMIN_ROLE, FARMER_ROLE
from .forms import positive_number, text_field, text_fields
from .models import FarmerProfile, User

auth_bp = Blueprint("auth", __name__)


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

        if len(fields["password"]) < 6:
            flash("Password must contain at least 6 characters.", "danger")
            return render_template("register.html", data=fields)

        if User.query.filter_by(username=fields["username"]).first():
            flash("That username is already in use.", "danger")
            return render_template("register.html", data=fields)

        try:
            farm_size = positive_number(fields["farm_size"])
        except ValueError:
            flash("Farm size must be a number greater than zero.", "danger")
            return render_template("register.html", data=fields)

        user = User(username=fields["username"], role=FARMER_ROLE)
        user.set_password(fields["password"])
        user.profile = FarmerProfile(
            full_name=fields["full_name"],
            contact_number=fields["contact_number"],
            location=fields["location"],
            farm_size=farm_size,
            banana_variety=fields["banana_variety"],
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
