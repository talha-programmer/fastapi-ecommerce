from sqlalchemy.orm import Session, joinedload

from db.models.product import Category, Product
from pydantic_schemas.product import ProductCreate



# def get_user(db: Session, user_id: int):
#     return db.query(Product).filter(Product.id == user_id).first()


def get_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()


def get_category(db: Session, category_id: int):
    return db.query(Category).filter(Category.id == category_id).first()


def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Product).offset(skip).options(joinedload(Product.category)).limit(limit).all()


def get_categories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Category).offset(skip).limit(limit).all()


def create_product(db: Session, product: ProductCreate):
    db_product = Product(
        title=product.title,
        description=product.description,
        discount_percentage=product.discount_percentage,
        stock=product.stock,
        price=product.price,
        rating=product.rating,
        brand=product.brand,
        category_id=product.category_id
    )

    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    return db_product 

