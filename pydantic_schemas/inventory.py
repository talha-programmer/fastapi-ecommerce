from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class InventoryBase(BaseModel):
    quantity: int
    product_id: int


class InventoryCreate(InventoryBase):
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    pass



class Inventory(InventoryBase):
    id: int
    created_at: datetime
    updated_at: datetime

    # This from_attributes must be provided for the pydantic to automatically detect the ORM. i.e. SQLAlchemy
    class Config:
        from_attributes = True
