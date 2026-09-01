"""Shared choices used by routes, models, and templates."""

ADMIN_ROLE = "admin"
FARMER_ROLE = "farmer"

REPORT_STATUSES = ("Reported", "Under Monitoring", "Resolved")
ASSISTANCE_STATUSES = ("Pending", "In Progress", "Completed")

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

