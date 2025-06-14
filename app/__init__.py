# app/__init__.py
import os

from flask import Blueprint, Flask
from flask_cors import CORS

from app.models import db, migrate


def create_app():
    app = Flask(__name__)

    # Config
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    CORS(
        app,
        resources={
            r"/*": {
                "origins": ["http://localhost:3003"],
                "methods": ["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"],
                "allow_headers": ["Content-Type", "Authorization"],
                "supports_credentials": True,
            }
        },
    )

    # Init extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Blueprints
    api_bp = Blueprint("api", __name__, url_prefix="/api")

    @api_bp.before_request
    def verify_report_secret():
        print("test")

    from app.routes import api

    api.init_app(api_bp)
    app.register_blueprint(api_bp)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=3003, debug=True)
