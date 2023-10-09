from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum, Text, Float
from sqlalchemy.orm import relationship

from ..db_setup import Base
from .mixins import Timestamp



class Order(Base, Timestamp):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, unique=True)
    quantity = Column(Integer, nullable=False)      # Positive for Increase in quantity, Negative for decrease
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    price = Column(Float, nullable=False)
    total_amount = Column(Float, nullable=False)
    discount_percentage = Column(Float, default=0, nullable=False)

    product = relationship("Product", back_populates="orders")  


