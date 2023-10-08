
from typing import Optional, List
from fastapi import Path, Depends, HTTPException
import fastapi
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from .utils.products import get_product, get_products, create_product, get_category, get_categories

from pydantic_schemas.product import Product, ProductCreate, Category
from db.db_setup import get_db


router = fastapi.APIRouter()

@router.get("/categories", response_model=List[Category])
async def all_categories(skip: int = 0, limit:int = 100, db: Session = Depends(get_db)):
    categories = get_categories(db, skip, limit)
    return categories 


@router.get("/products", response_model=List[Product])
async def all_products(skip: int = 0, limit:int = 100, db: Session = Depends(get_db)):
    products = get_products(db, skip, limit)
    return products 


@router.post("/products", status_code=201)
async def create(product: ProductCreate, db: Session = Depends(get_db)):
    category = get_category(db, product.category_id)
    if category is None:
        raise HTTPException(422, "Invalid category id")
    return create_product(db, product)


@router.get("/products/{id}")
async def show_product(
    id: int = Path(..., description="The ID of the product"),  
    db: Session = Depends(get_db)
):      
    product = get_product(db, id)
    if product is None:
        raise HTTPException(404, "Invalid product id")
    return product 