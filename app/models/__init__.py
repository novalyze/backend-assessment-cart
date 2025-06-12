from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db: SQLAlchemy = SQLAlchemy()
migrate = Migrate()

from .cart import Cart
from .cart_item import CartItem
from .product import Product
