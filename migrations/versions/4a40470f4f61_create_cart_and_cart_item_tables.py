"""create carts, cart_items, products tables and seed data

Revision ID: 4a40470f4f61
Revises:
Create Date: 2025-06-11 11:21:18.068925

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "4a40470f4f61"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # 1) Create carts table
    op.create_table(
        "carts",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("status", sa.String(length=20), nullable=False),
    )

    # 2) Create products table
    op.create_table(
        "products",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("cost", sa.Numeric(10, 2), nullable=False),
        sa.Column("description", sa.String(length=255), nullable=False),
    )

    # 3) Create cart_items with both FKs
    op.create_table(
        "cart_items",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("cart_id", sa.Integer(), nullable=False),
        sa.Column("product_id", sa.Integer(), nullable=False),
        sa.Column("quantity", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["cart_id"], ["carts.id"], name="fk_cart_items_cart"),
        sa.ForeignKeyConstraint(
            ["product_id"], ["products.id"], name="fk_cart_items_product"
        ),
    )

    # 4) Seed products
    products_table = sa.table(
        "products",
        sa.column("id", sa.Integer),
        sa.column("cost", sa.Numeric),
        sa.column("description", sa.String),
    )
    op.bulk_insert(
        products_table,
        [
            {"id": 1, "cost": 19.99, "description": "Apple iWidget"},
            {"id": 2, "cost": 5.49, "description": "Banana Gadget"},
            {"id": 3, "cost": 12.00, "description": "Cherry Doohickey"},
        ],
    )

    # 5) Seed carts
    carts_table = sa.table(
        "carts",
        sa.column("id", sa.Integer),
        sa.column("status", sa.String),
    )
    op.bulk_insert(
        carts_table,
        [
            {"id": 1, "status": "open"},
            {"id": 2, "status": "submitted"},
        ],
    )

    # 6) Seed cart_items
    items_table = sa.table(
        "cart_items",
        sa.column("id", sa.Integer),
        sa.column("cart_id", sa.Integer),
        sa.column("product_id", sa.Integer),
        sa.column("quantity", sa.Integer),
    )
    op.bulk_insert(
        items_table,
        [
            {"id": 1, "cart_id": 1, "product_id": 1, "quantity": 2},
            {"id": 2, "cart_id": 1, "product_id": 2, "quantity": 3},
            {"id": 3, "cart_id": 2, "product_id": 3, "quantity": 1},
        ],
    )


def downgrade() -> None:
    # 1) Remove seeded data
    op.execute("DELETE FROM cart_items")
    op.execute("DELETE FROM carts")
    op.execute("DELETE FROM products")

    # 2) Drop tables & constraints in reverse order
    op.drop_constraint("fk_cart_items_product", "cart_items", type_="foreignkey")
    op.drop_constraint("fk_cart_items_cart", "cart_items", type_="foreignkey")
    op.drop_table("cart_items")
    op.drop_table("products")
    op.drop_table("carts")
