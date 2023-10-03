from sqlalchemy.orm import Session

from db.models.product import Category, Product
from sqlalchemy.future import select



# def get_user(db: Session, user_id: int):
#     return db.query(Product).filter(Product.id == user_id).first()


def get_product(db: Session, product_id: int):
    query = select(Product).where(Product.id == product_id)
    result =  db.execute(query)
    return result.scalar_one_or_none()



def get_products(db: Session, skip: int = 0, limit: int = 100):
    query = select(Product).offset(skip).limit(limit)
    result =  db.execute(query)
    return result.all()


# def create_user(db: Session, user: UserCreate):
#     db_user = Product(email=user.email, role=user.role)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user