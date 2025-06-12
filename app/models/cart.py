from . import db


class Cart(db.Model):
    __tablename__ = "carts"
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(
        db.String(20), nullable=False, default="open"
    )  # "open", "closed", etc.
