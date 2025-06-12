# app/api/routes/__init__.py
from flask_restx import Api

from app.routes.cart import cart_ns

# Import all namespaces from the individual route modules
from app.routes.health import health_ns
from app.routes.products import products_ns

# Create an API instance
api = Api(
    title="Novalyze API", version="1.0", description="Production API for Novalyze App"
)

# Register namespaces with custom paths
api.add_namespace(health_ns, path="/health")
api.add_namespace(cart_ns, path="/cart")
api.add_namespace(products_ns, path="/products")
