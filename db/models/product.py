import enum
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum, Text, Float
from sqlalchemy.orm import relationship

from ..db_setup import Base
from .mixins import Timestamp


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)

    products = relationship("Product", back_populates="owner")  


class Product(Timestamp, Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)
    price = Column(Float, nullable=False)
    discount_percentage = Column(Float, nullable=False)
    rating = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False, default=0)
    brand = Column(String(100), nullable=False)

    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)

    category = relationship("Category", back_populates="products")   

