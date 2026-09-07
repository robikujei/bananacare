"""
BananaCare application factory.

Initializes Flask extensions (SQLAlchemy, Flask-Login) and registers
blueprints. Kept free of route/model logic per project structure.
"""

import logging
import os

from dotenv import load_dotenv
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
login_manager = LoginManager()

logger = logging.getLogger(__name__)


def create_app(test_config: dict | None = None) -> Flask:
    """Application factory for BananaCare.

    Args:
        test_config: Optional config overrides, used for testing.

    Returns:
        A configured Flask application instance.
    """
    load_dotenv()
    app = Flask(__name__)

    secret_key = os.getenv("SECRET_KEY", "dev-only-change-me")
    env = os.getenv("FLASK_ENV", "production")
    if secret_key == "dev-only-change-me" and env == "production":
        logger.warning(
            "SECRET_KEY is unset in a production environment. "
            "Set the SECRET_KEY environment variable before deploying."
        )

    app.config.update(
        SECRET_KEY=secret_key,
        SQLALCHEMY_DATABASE_URI=os.getenv(
            "DATABASE_URL", "sqlite:///bananacare.db"
        ),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        SQLALCHEMY_ENGINE_OPTIONS={"pool_pre_ping": True},
    )

    if test_config:
        app.config.update(test_config)

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "auth.farmer_login"
    login_manager.login_message = "Please log in to access this page."
    login_manager.login_message_category = "info"

    # Local imports avoid circular imports between models/blueprints and `db`.
    from .models import User

    @login_manager.user_loader
    def load_user(user_id: str) -> User | None:
        if not user_id or not user_id.isdigit():
            return None
        return db.session.get(User, int(user_id))

    from .auth import auth_bp
    from .main import main_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)

    # db.create_all() is fine for SQLite dev use, but should not run
    # unconditionally against a production Postgres database where
    # migrations (e.g. Flask-Migrate) should own schema changes instead.
    if not test_config or test_config.get("CREATE_TABLES", True):
        with app.app_context():
            db.create_all()

    return app