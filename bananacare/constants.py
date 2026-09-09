# constants.py
"""Shared choices used by routes, models, and templates."""

ADMIN_ROLE = "admin"
FARMER_ROLE = "farmer"

REPORT_STATUSES = ("Reported", "Under Monitoring", "Resolved")
ASSISTANCE_STATUSES = ("Pending", "In Progress", "Completed")

# Named alias for the terminal assistance status, so routes don't rely on a
# magic index (ASSISTANCE_STATUSES[-1]) to detect "done".
ASSISTANCE_COMPLETED = ASSISTANCE_STATUSES[-1]

PROBLEM_TYPES = (
    "Fusarium Wilt",
    "Sigatoka",
    "Pest Infestation",
    "Weather Damage",
    "Soil Condition",
    "Other",
)

ASSISTANCE_TYPES = (
    "Seedlings",
    "Fertilizer",
    "Training",
    "Disease-Control Support",
    "Farm Visit",
    "Other",
)

# Maximum lengths for free-text fields, mirroring the String() column sizes
# declared in models.py. Validating here prevents an over-long value from
# reaching the database, where PostgreSQL (unlike SQLite) enforces VARCHAR
# limits and would raise an unhandled DataError instead of a friendly error.
MAX_LENGTHS = {
    "username": 50,
    "full_name": 100,
    "contact_number": 20,
    "location": 150,
    "banana_variety": 80,
}