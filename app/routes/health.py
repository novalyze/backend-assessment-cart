# app/routes/health.py


from flask import Response, jsonify
from flask_restx import Namespace, Resource
from sqlalchemy import text

from app.models import db

# Create a dedicated namespace for health checks
health_ns = Namespace("health", description="Health Check Endpoints")


@health_ns.route("", strict_slashes=False)
@health_ns.route("/", strict_slashes=False)
class HealthCheck(Resource):
    @health_ns.doc("check_health")
    def get(self) -> Response:
        return jsonify({"msg": "status: OK"})


@health_ns.route("/db", strict_slashes=False)
@health_ns.route("/db/", strict_slashes=False)
class HealthDB(Resource):
    @health_ns.doc("check_db_health")
    def get(self) -> tuple:
        try:
            # Simple query to test DB connection
            db.session.execute(text("SELECT 1"))
            return {"db": "ok"}, 200
        except Exception as e:
            return {"db": "error", "message": str(e)}, 500
