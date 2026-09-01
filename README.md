# BananaCare

BananaCare is a small Flask information system for managing banana farm records, monitoring farm conditions, and tracking farmer assistance. It was designed as a reusable classroom template rather than for a particular real-world location.

## Features

1. Farmer and farm record management
2. Disease and farm-condition monitoring
3. Assistance and recommendation tracking
4. Separate Farmer and Admin login routes
5. Input validation, role protection, and automated tests

## Quick setup (PostgreSQL)

1. Create a PostgreSQL database named `bananacare` using pgAdmin or:

   ```sql
   CREATE DATABASE bananacare;
   ```

2. In PowerShell, create the environment and install packages:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   python -m pip install -r requirements.txt
   Copy-Item .env.example .env
   ```

3. Edit `.env` and put your PostgreSQL username and password in `DATABASE_URL`.

4. Create sample accounts and run the system:

   ```powershell
   python seed.py
   python run.py
   ```

5. Open `http://127.0.0.1:5000`.

Demo accounts after running `seed.py`:

- Admin: `admin` / `admin123`
- Farmer: `farmer1` / `farmer123`

Change these passwords if the project is ever used beyond a local classroom demonstration.

## Testing

Tests use a temporary in-memory SQLite database, so PostgreSQL does not need to be running:

```powershell
python -m unittest discover -s tests -v
```

## Routes

- `/farmer/login` — farmer sign-in
- `/farmer/register` — farmer registration
- `/admin/login` — staff/admin sign-in
- `/farmer/dashboard` — farmer records and request history
- `/admin/dashboard` — consolidated monitoring and status management

## Project structure

```text
bananacare/
  templates/       HTML interface
  static/          CSS styling
  __init__.py      application setup
  auth.py          registration and login routes
  main.py          dashboards, farm, report, and assistance routes
  models.py        database tables
  constants.py     roles and valid status/type choices
  forms.py         shared form parsing helpers
tests/             automated test cases
run.py             development server
seed.py            sample accounts and records
```

See [ARCHITECTURE.md](ARCHITECTURE.md) for module responsibilities, request/data flow, and important functions.

## Refactoring comparison

The source immediately before the maintainability refactor is preserved in `backups/bananacare-pre-refactor/`. It is intended for comparison and assessment evidence; run the application from the project root.

