"""Small form parsing helpers shared by the route modules."""

from datetime import date

from flask import request


def text_field(name):
    """Return a form value with surrounding whitespace removed."""
    return request.form.get(name, "").strip()


def text_fields(*names):
    """Return trimmed form values keyed by field name."""
    return {name: text_field(name) for name in names}


def positive_number(value):
    """Parse a number and reject zero and negative values."""
    number = float(value)
    if number <= 0:
        raise ValueError("Value must be greater than zero.")
    return number


def optional_number(value):
    """Parse an optional number; a blank value becomes None."""
    return float(value) if value else None


def optional_date(value):
    """Parse an optional ISO date; a blank value becomes None."""
    return date.fromisoformat(value) if value else None

