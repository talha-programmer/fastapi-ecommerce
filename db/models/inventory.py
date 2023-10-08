from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum, Text, Float
from sqlalchemy.orm import relationship

from ..db_setup import Base
from .mixins import Timestamp



class Inventory(Base, Timestamp):
    __tablename__ = "inventories"

    id = Column(Integer, primary_key=True, unique=True)
    quantity = Column(Integer)      # Positive for Increase in quantity, Negative for decrease
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)

    product = relationship("Product", back_populates="inventories")  


