from typing import Optional, List
from datetime import date

from fastapi import Path, Depends, HTTPException, Query
import fastapi
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from .utils.orders import get_orders, get_revenue
from pydantic_schemas.order import Order, OrderCreate
from db.db_setup import get_db


router = fastapi.APIRouter()


@router.get("/orders", response_model=List[Order])
async def all_orders(
    skip: int = 0,
    limit: int = 100,
    product_id: int = 0,
    category_id: int = 0,
    start_date: date = date(2000, 1, 1),
    end_date: date = date.today(),
    db: Session = Depends(get_db),
):
    orders = get_orders(db, skip, limit, product_id=product_id, start_date=start_date, end_date=end_date, category_id=category_id)
    return orders


@router.get("/revenue")
async def revenue(interval: str = Query('year', description="Allowed values: year, month, week"), product_id: int = 0,  db: Session = Depends(get_db)):
    revenue = get_revenue(db, interval=interval, product_id=product_id)
    return revenue
