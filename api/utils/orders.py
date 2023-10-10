import random
from datetime import datetime
import json

from sqlalchemy.orm import Session, join
from sqlalchemy import func, text, select
from pydantic_schemas.order import OrderCreate
from pydantic_schemas.product import Product

from ..products import get_products, get_product
from helper import generate_random_time
from db.models.order import Order
from db.models.product import Product as ProductModel


def seed_order(db: Session):
    products = get_products(db, 0, 1000)
    for product in products:
        generate_orders(db, product)


# Generate 30 order records for each product by default
def generate_orders(db: Session, product: Product, entries: int = 30):
    for i in range(entries):
        quantity = random.randint(1, 10)
        apply_discount = bool(random.randint(0, 1))
        update_time = generate_random_time(datetime(2020, 1, 1), datetime.now())
        order = OrderCreate(
            quantity=quantity,
            product_id=product.id,
            created_at=update_time,
            updated_at=update_time,
        )
        create_order(db, order, apply_discount)



def create_order(db: Session, order: OrderCreate, apply_discount: bool = False):
    product = get_product(db, order.product_id)
    price = product.price

    discount = 0
    if apply_discount == True:
        discount = product.discount_percentage
        price -= (discount / 100) * product.price
    total_amount = price * order.quantity

    db_order = Order(
        quantity=order.quantity,
        product_id=order.product_id,
        created_at=order.created_at,
        updated_at=order.updated_at,
        price=price,
        discount_percentage=discount,
        total_amount=total_amount,
    )

    db.add(db_order)
    db.commit()
    db.refresh(db_order)

    return db_order



def get_orders(
    db: Session,
    skip: int = 0,
    limit: int = 100,
    product_id: int = 0,
    category_id: int = 0,
    start_date: datetime = None,
    end_date: datetime = None,
):
    query = db.query(Order)
    if product_id > 0:
        query = query.where(Order.product_id == product_id)

    if category_id > 0:
        query = query.join(ProductModel).where(ProductModel.category_id == category_id)

    if start_date is not None:
        query = query.where(Order.created_at >= start_date)

    if end_date is not None:
        query = query.where(Order.created_at <= end_date)

    return query.order_by(Order.created_at).offset(skip).limit(limit).all()



def get_revenue(
    db: Session,
    product_id: int = 0,
    interval: str = 'week'    # month, week, year
):

    period = "YEAR(created_at)"
    if interval == 'month':
        period = "DATE_FORMAT(created_at, '%M, %Y')"
    elif interval == 'week':
        period = "DATE_FORMAT(created_at, 'Week %v, %b, %Y')"

    product_condition = ""
    if product_id > 0:
        product_condition = f"WHERE product_id = {product_id}"

    query = text(f"SELECT {period} as period, SUM(total_amount) as revenue FROM orders {product_condition} GROUP BY period ORDER BY MIN(created_at)")

    results = db.execute(query).fetchall()


    results = [{'period': row.period, 'revenue': round(row.revenue, 2)} for row in results]

    return results

