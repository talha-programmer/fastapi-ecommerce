from datetime import datetime

from pydantic import BaseModel


class UserBase(BaseModel):
    email: str
    role: int


class UserCreate(UserBase):
    ...


class User(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime

    # This orm_mode must be provided for the pydantic to automatically detect the ORM. i.e. SQLAlchemy
    class Config:
        from_attributes = True