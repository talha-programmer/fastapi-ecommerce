"""orders table

Revision ID: 481b00f5d0e1
Revises: 5c65d0c0ad01
Create Date: 2023-10-09 13:14:26.134408

"""
from typing import Sequence, Union
from datetime import datetime

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

from db.db_setup import get_db
from api.utils.orders import seed_order

# revision identifiers, used by Alembic.
revision: str = '481b00f5d0e1'
down_revision: Union[str, None] = '5c65d0c0ad01'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

db = get_db()

def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('orders',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('quantity', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('product_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('price', mysql.FLOAT(), nullable=False),
    sa.Column('discount_percentage', mysql.FLOAT(), nullable=False),
    sa.Column('total_amount', mysql.FLOAT(), nullable=False),
    sa.Column('created_at', mysql.DATETIME(), nullable=False, default=datetime.utcnow()),
    sa.Column('updated_at', mysql.DATETIME(), nullable=False, default=datetime.utcnow()),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], name='orders_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###


    seed_order(next(db))


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('orders')
    # ### end Alembic commands ###