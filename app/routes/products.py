from flask_restx import Namespace, Resource

from app.models import Product

# Create a dedicated namespace for product endpoints
products_ns = Namespace("products", description="Product Endpoints")


@products_ns.route("", strict_slashes=False)
@products_ns.route("/", strict_slashes=False)
class ProductList(Resource):
    @products_ns.doc("list_products")
    def get(self) -> tuple:
        """
        GET /api/products
        Return the full list of products.
        """
        products = Product.get_all_products()
        return {"msg": "Successfully retrieved all products", "products": products}, 200
