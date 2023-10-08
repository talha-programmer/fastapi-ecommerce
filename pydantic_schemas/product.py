from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class Category(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


class ProductBase(BaseModel):
    title: str
    description: str
    price: float
    discount_percentage: Optional[float] = 0
    rating: float
    stock: Optional[int] = 0
    brand: str
    category_id: int



class ProductCreate(ProductBase):
    ...



class Product(ProductBase):
    id: int
    created_at: datetime
    updated_at: datetime
    category: Category

    # This from_attributes must be provided for the pydantic to automatically detect the ORM. i.e. SQLAlchemy
    class Config:
        from_attributes = True
