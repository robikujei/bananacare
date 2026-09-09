# main.py
from datetime import date
from functools import wraps

from flask import Blueprint, abort, flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from sqlalchemy.orm import joinedload

from . import db
from .constants import (
    ADMIN_ROLE,
    ASSISTANCE_COMPLETED,
    ASSISTANCE_STATUSES,
    ASSISTANCE_TYPES,
    FARMER_ROLE,
    MAX_LENGTHS,
    PROBLEM_TYPES,
    REPORT_STATUSES,
)
from .forms import (
    bounded_text,
    choice,
    optional_date,
    optional_number,
    positive_number,
    text_field,
    text_fields,
)
from .models import Assistance, DiseaseReport, FarmerProfile

main_bp = Blueprint("main", __name__)


def role_required(role):
    """Restrict a view to authenticated users with the required role."""
    def decorator(view):
        @wraps(view)
        @login_required
        def wrapped(*args, **kwargs):
            if current_user.role != role:
                abort(403)
            return view(*args, **kwargs)

        return wrapped

    return decorator


@main_bp.route("/")
def index():
    return render_template("index.html")


@main_bp.route("/dashboard")
@login_required
def dashboard():
    return redirect(url_for(f"main.{current_user.role}_dashboard"))


@main_bp.route("/farmer/dashboard")
@role_required(FARMER_ROLE)
def farmer_dashboard():
    profile = current_user.profile
    reports = (
        DiseaseReport.query.filter_by(farmer_id=profile.id)
        .order_by(DiseaseReport.id.desc())
        .all()
    )
    assistance_records = (
        Assistance.query.filter_by(farmer_id=profile.id)
        .order_by(Assistance.id.desc())
        .all()
    )
    return render_template(
        "farmer_dashboard.html",
        profile=profile,
        reports=reports,
        requests=assistance_records,
    )


@main_bp.route("/farmer/profile", methods=["GET", "POST"])
@role_required(FARMER_ROLE)
def farmer_profile():
    profile = current_user.profile
    if request.method == "POST":
        fields = text_fields(
            "full_name",
            "contact_number",
            "location",
            "farm_size",
            "banana_variety",
            "planting_date",
            "estimated_production",
        )
        required_fields = (
            fields["full_name"],
            fields["contact_number"],
            fields["location"],
            fields["farm_size"],
            fields["banana_variety"],
        )

        if not all(required_fields):
            flash("All required fields must be completed.", "danger")
        else:
            try:
                full_name = bounded_text(
                    fields["full_name"], "Full name", MAX_LENGTHS["full_name"]
                )
                contact_number = bounded_text(
                    fields["contact_number"],
                    "Contact number",
                    MAX_LENGTHS["contact_number"],
                )
                location = bounded_text(
                    fields["location"], "Location", MAX_LENGTHS["location"]
                )
                banana_variety = bounded_text(
                    fields["banana_variety"],
                    "Banana variety",
                    MAX_LENGTHS["banana_variety"],
                )
                farm_size = positive_number(fields["farm_size"])
                planting_date = optional_date(fields["planting_date"])
                estimated_production = optional_number(fields["estimated_production"])

                profile.full_name = full_name
                profile.contact_number = contact_number
                profile.location = location
                profile.farm_size = farm_size
                profile.banana_variety = banana_variety
                profile.planting_date = planting_date
                profile.estimated_production = estimated_production
                db.session.commit()
                flash("Farm profile updated.", "success")
                return redirect(url_for("main.farmer_dashboard"))
            except (ValueError, TypeError) as exc:
                flash(str(exc) or "Enter valid values for every field.", "danger")

    return render_template("profile_form.html", profile=profile)


@main_bp.route("/farmer/reports/new", methods=["GET", "POST"])
@role_required(FARMER_ROLE)
def new_report():
    if request.method == "POST":
        try:
            affected_area = positive_number(text_field("affected_area"))
            problem_type = choice(text_field("problem_type"), PROBLEM_TYPES, "problem type")
            description = text_field("description")
            farm_size = float(current_user.profile.farm_size)

            if affected_area > farm_size or not description:
                raise ValueError("Affected area cannot exceed farm size.")

            report = DiseaseReport(
                farmer_id=current_user.profile.id,
                problem_type=problem_type,
                affected_area=affected_area,
                description=description,
                date_reported=date.today(),
            )
            db.session.add(report)
            db.session.commit()
            flash("Farm condition report submitted.", "success")
            return redirect(url_for("main.farmer_dashboard"))
        except ValueError:
            flash(
                "Complete every field with a valid problem type. Affected area "
                "must be positive and cannot exceed farm size.",
                "danger",
            )

    return render_template("report_form.html", problem_types=PROBLEM_TYPES)


@main_bp.route("/farmer/assistance/new", methods=["GET", "POST"])
@role_required(FARMER_ROLE)
def new_assistance():
    if request.method == "POST":
        try:
            assistance_type = choice(
                text_field("assistance_type"), ASSISTANCE_TYPES, "assistance type"
            )
        except ValueError:
            flash("Please select a valid assistance type.", "danger")
        else:
            request_details = text_field("recommendation")
            assistance = Assistance(
                farmer_id=current_user.profile.id,
                assistance_type=assistance_type,
                recommendation=request_details,
            )
            db.session.add(assistance)
            db.session.commit()
            flash("Assistance request submitted.", "success")
            return redirect(url_for("main.farmer_dashboard"))

    return render_template("assistance_form.html", assistance_types=ASSISTANCE_TYPES)


@main_bp.route("/admin/dashboard")
@role_required(ADMIN_ROLE)
def admin_dashboard():
    farmers = FarmerProfile.query.order_by(FarmerProfile.full_name).all()
    # Eager-load the farmer relationship: the dashboard shows a farmer name
    # on every report/assistance row, so without this each row lazily fires
    # its own SELECT (classic N+1 — e.g. 50 reports = 51 queries instead of 2).
    reports = (
        DiseaseReport.query.options(joinedload(DiseaseReport.farmer))
        .order_by(DiseaseReport.id.desc())
        .all()
    )
    assistance_records = (
        Assistance.query.options(joinedload(Assistance.farmer))
        .order_by(Assistance.id.desc())
        .all()
    )

    return render_template(
        "admin_dashboard.html",
        farmers=farmers,
        reports=reports,
        requests=assistance_records,
        report_statuses=REPORT_STATUSES,
        assistance_statuses=ASSISTANCE_STATUSES,
    )


@main_bp.route("/admin/reports/<int:report_id>", methods=["POST"])
@role_required(ADMIN_ROLE)
def update_report(report_id):
    report = db.get_or_404(DiseaseReport, report_id)
    status = request.form.get("status")
    if status not in REPORT_STATUSES:
        abort(400)

    report.status = status
    report.remarks = text_field("remarks")
    db.session.commit()
    flash("Report status updated.", "success")
    return redirect(url_for("main.admin_dashboard"))


@main_bp.route("/admin/assistance/<int:request_id>", methods=["POST"])
@role_required(ADMIN_ROLE)
def update_assistance(request_id):
    item = db.get_or_404(Assistance, request_id)
    status = request.form.get("status")
    if status not in ASSISTANCE_STATUSES:
        abort(400)

    item.status = status
    item.recommendation = text_field("recommendation")

    if status == ASSISTANCE_COMPLETED:
        # Only stamp the completion date the first time it's marked
        # Completed — see Changes below for why this matters.
        if item.date_provided is None:
            item.date_provided = date.today()
    else:
        item.date_provided = None

    db.session.commit()
    flash("Assistance record updated.", "success")
    return redirect(url_for("main.admin_dashboard"))