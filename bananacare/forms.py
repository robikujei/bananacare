# forms.py
"""Small form parsing helpers shared by the route modules."""

from datetime import date

from flask import request

# All Numeric(10, 2) columns in the schema (farm_size, affected_area,
# estimated_production) allow at most 8 integer digits before the decimal
# point. A value at or above this bound would be rejected by PostgreSQL
# with an unhandled DataError, so it's validated here up front instead.
MAX_NUMERIC_VALUE = 10**8


def text_field(name):
    """Return a form value with surrounding whitespace removed."""
    return request.form.get(name, "").strip()


def text_fields(*names):
    """Return trimmed form values keyed by field name."""
    return {name: text_field(name) for name in names}


def _check_numeric_bounds(number):
    if number >= MAX_NUMERIC_VALUE:
        raise ValueError(f"Value must be less than {MAX_NUMERIC_VALUE:,}.")
    return number


def positive_number(value):
    """Parse a number, rejecting zero, negative, and out-of-range values."""
    number = float(value)
    if number <= 0:
        raise ValueError("Value must be greater than zero.")
    return _check_numeric_bounds(number)


def optional_number(value):
    """Parse an optional number; a blank value becomes None."""
    if not value:
        return None
    number = float(value)
    if number < 0:
        raise ValueError("Value cannot be negative.")
    return _check_numeric_bounds(number)


def optional_date(value):
    """Parse an optional ISO date; a blank value becomes None."""
    return date.fromisoformat(value) if value else None


def choice(value, allowed, label):
    """Validate that a submitted value is one of a fixed set of choices."""
    if value not in allowed:
        raise ValueError(f"Select a valid {label}.")
    return value


def bounded_text(value, label, max_length):
    """Validate that text fits within a database column's length limit."""
    if len(value) > max_length:
        raise ValueError(f"{label} must be {max_length} characters or fewer.")
    return value