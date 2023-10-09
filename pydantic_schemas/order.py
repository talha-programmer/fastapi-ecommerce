from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class OrderBase(BaseModel):
    quantity: int
    product_id: int



class OrderCreate(OrderBase):
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    discount_percentage: Optional[float] = None



class Order(OrderBase):
    id: int
    price: float
    discount_percentage: float
    total_amount: float
    created_at: datetime
    updated_at: datetime

    # This from_attributes must be provided for the pydantic to automatically detect the ORM. i.e. SQLAlchemy
    class Config:
        from_attributes = True
