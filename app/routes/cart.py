from flask import Response
from flask_restx import Namespace, Resource

# Create a dedicated namespace for cart operations
cart_ns = Namespace("cart", description="Cart Management Endpoints")


@cart_ns.route("/<int:cart_id>", strict_slashes=False)
class CartResource(Resource):
    @cart_ns.doc("get_cart")
    def get(self) -> Response:
        """
        GET /api/cart/
        Return the resources (items) in given cart_id cart.
        """
        raise NotImplementedError("get_cart endpoint not implemented")


@cart_ns.route("/update", strict_slashes=False)
class PostCartResource(Resource):
    @cart_ns.doc("set_cart")
    def post(self) -> Response:
        """
        POST /api/cart/
        Set or update the resources in a cart.
        Expects JSON payload:
            {"cart_id: 1, "items": [{"product_id": X, "quantity": Y}, ...]}
        """
        raise NotImplementedError("set_cart endpoint not implemented")


@cart_ns.route("/submit", strict_slashes=False)
class CartSubmitResource(Resource):
    @cart_ns.doc("submit_cart")
    def post(self) -> Response:
        """
        POST /api/cart/submit
        Submit the cart: mark status and trigger submission logic.
        Expects JSON payload:
            {"cart_id: 1}
        """
        raise NotImplementedError("submit_cart endpoint not implemented")
