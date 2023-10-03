
from typing import Optional, List
from fastapi import Path, Query, Depends, HTTPException
import fastapi
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from .utils.products import get_product, get_products
from db.db_setup import get_db


router = fastapi.APIRouter()


@router.get("/products")
async def index(skip: int = 0, limit:int = 100, db: Session = Depends(get_db)):
    products = get_products(db, skip, limit)
    return products 



# In the post request we can define path parameters like that: app.post("/users")
# @router.post("/users", response_model=User, status_code=201)
# async def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
#     return create_user(db, user)


@router.get("/products/{id}")
async def show(
    id: int = Path(..., description="The ID of the product"),  
    db: Session = Depends(get_db)
):      
    product = get_product(db, id)
    if product is None:
        raise HTTPException(404, "Invalid product id")
    return product 