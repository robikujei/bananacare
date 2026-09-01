# BananaCare Architecture

## Overview

BananaCare is a small server-rendered Flask application. It deliberately uses a simple structure: the browser sends a request to a Flask route, the route validates form data and reads or writes SQLAlchemy models, then a Jinja template renders the response. There is no separate frontend build process or unnecessary service layer.

## Main modules

| Module | Responsibility |
|---|---|
| `bananacare/__init__.py` | Application factory, configuration, database/login initialization, and blueprint registration |
| `bananacare/auth.py` | Farmer registration, Farmer/Admin login, and logout |
| `bananacare/main.py` | Public page, role dashboards, farm profile, reports, assistance, and Admin updates |
| `bananacare/models.py` | `User`, `FarmerProfile`, `DiseaseReport`, and `Assistance` database models |
| `bananacare/constants.py` | Shared roles, statuses, problem types, and assistance types |
| `bananacare/forms.py` | Reusable trimming and number/date parsing helpers |
| `bananacare/templates/` | Jinja HTML views rendered by Flask |
| `bananacare/static/` | Shared CSS presentation |
| `seed.py` | Idempotent creation of demonstration users and records |
| `tests/test_app.py` | Regression tests using an isolated in-memory database |

## Data model

```text
User (one) ─── (zero or one) FarmerProfile
                              │
                              ├── (many) DiseaseReport
                              └── (many) Assistance
```

- Admin users have a `User` row and no farmer profile.
- Farmer users have one profile containing farmer and farm details.
- Reports and assistance records belong to the farmer profile.
- Deleting a Farmer profile cascades to its reports and assistance records.

## Request and data flow

### Farmer registration

1. `/farmer/register` receives the submitted form.
2. `text_fields()` trims the required values.
3. The route checks completeness, password length, username uniqueness, and farm size.
4. A `User` and related `FarmerProfile` are committed together.
5. The user is redirected to `/farmer/login`.

### Authentication and authorization

1. Separate Farmer and Admin routes call `_login(expected_role)`.
2. The user is looked up by both username and expected role.
3. Werkzeug verifies the stored password hash; Flask-Login creates the session.
4. `role_required(role)` protects role-specific pages and returns HTTP 403 for the wrong role.

### Farm condition report

1. The Farmer submits `/farmer/reports/new`.
2. The route validates required text and ensures affected area is positive and no larger than farm size.
3. A `DiseaseReport` begins with `Reported` status.
4. Admin updates are restricted to values in `REPORT_STATUSES`.
5. Updated status and remarks appear on the Farmer dashboard.

### Assistance request

1. The Farmer submits `/farmer/assistance/new`.
2. The request is stored with `Pending` status.
3. Admin can move it through the values in `ASSISTANCE_STATUSES` and add recommendations.
4. Completing the request records the current date; moving it out of Completed clears that date.

## Important functions

| Function | Purpose |
|---|---|
| `create_app(test_config=None)` | Builds and configures the Flask application; tests override database and secret settings here |
| `_login(expected_role)` | Shares login logic while keeping separate portal routes |
| `role_required(role)` | Combines login enforcement with role authorization |
| `text_field()` / `text_fields()` | Consistently strip surrounding whitespace from submitted values |
| `positive_number()` | Parses numeric values that must be above zero |
| `optional_number()` / `optional_date()` | Convert blank optional fields to `None` and parse provided values |
| `User.set_password()` / `check_password()` | Hash and verify passwords without storing plaintext |

## Configuration and database

`create_app()` loads `.env` and reads:

- `SECRET_KEY` for signed Flask sessions.
- `DATABASE_URL` for SQLAlchemy.

The documented production-style local setup uses PostgreSQL. If `DATABASE_URL` is absent, the application uses `instance/bananacare.db` as a convenient SQLite classroom/demo fallback. Tests always replace this setting with an isolated in-memory SQLite database.

## Maintenance guidance

- Add or rename status/type choices in `constants.py`, not independently in routes and templates.
- Put new HTTP workflow logic in the appropriate existing blueprint.
- Use `forms.py` for small reusable parsing rules; keep workflow-specific validation near its route.
- Add a regression test whenever expected behavior changes or a bug is fixed.
- Avoid committing `.env`, database passwords, or real farmer data.

