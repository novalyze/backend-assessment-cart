from . import db


class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    cost = db.Column(db.Numeric(10, 2), nullable=False)
    description = db.Column(db.String(255), nullable=False)

    @classmethod
    def get_all_products(cls) -> list:
        """
        Fetch all products from the database.

        Returns:
            List[Product]: list of all Product instances
        """
        products = cls.query.all()
        serialized = [
            {"id": p.id, "cost": float(p.cost), "description": p.description}
            for p in products
        ]
        return serialized
