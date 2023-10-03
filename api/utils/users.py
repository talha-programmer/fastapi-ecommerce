from sqlalchemy.orm import Session

from db.models.user import User
from pydantic_schemas.user import UserCreate
from sqlalchemy.future import select



# def get_user(db: Session, user_id: int):
#     return db.query(User).filter(User.id == user_id).first()


def get_user(db: Session, user_id: int):
    query = select(User).where(User.id == user_id)
    result =  db.execute(query)
    return result.scalar_one_or_none()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def create_user(db: Session, user: UserCreate):
    db_user = User(email=user.email, role=user.role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user